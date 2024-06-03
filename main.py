from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import os

class FileRenameApp(App):
    directory = ObjectProperty(None)
    config_file = 'directory_config.txt'

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Select a directory')
        layout.add_widget(self.label)

        select_dir_button = Button(text='Select Directory')
        select_dir_button.bind(on_press=self.select_directory)
        layout.add_widget(select_dir_button)

        rename_button = Button(text='Rename to .mp4')
        rename_button.bind(on_press=self.rename_to_mp4)
        layout.add_widget(rename_button)

        revert_button = Button(text='Revert to .txt')
        revert_button.bind(on_press=self.revert_to_txt)
        layout.add_widget(revert_button)

        self.load_directory()

        return layout

    def load_directory(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.directory = file.read().strip()
                if self.directory:
                    self.label.text = f'Selected directory: {self.directory}'
                else:
                    self.label.text = 'Select a directory'
        else:
            self.label.text = 'Select a directory'

    def save_directory(self):
        with open(self.config_file, 'w') as file:
            file.write(self.directory if self.directory else '')

    def select_directory(self, instance):
        filechooser = FileChooserIconView(path='/', filters=['*'], dirselect=True)
        submit_button = Button(text='Submit', size_hint_y=None, height='48dp')
        
        def on_submit(instance):
            selection = filechooser.selection
            if selection:
                self.set_directory(selection)
            self.popup.dismiss()
        
        submit_button.bind(on_press=on_submit)
        
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(filechooser)
        popup_layout.add_widget(submit_button)
        
        self.popup = Popup(title='Select Directory', content=popup_layout, size_hint=(0.9, 0.9))
        self.popup.open()

    def set_directory(self, selection):
        if selection:
            self.directory = selection[0]
            self.label.text = f'Selected directory: {self.directory}'
            self.save_directory()
        else:
            self.label.text = 'No directory selected'

    def rename_to_mp4(self, instance):
        if not self.directory:
            self.label.text = 'Select a directory first'
            return

        if os.path.exists(self.directory):
            try:
                for filename in os.listdir(self.directory):
                    if filename.endswith('.txt'):
                        base = os.path.splitext(filename)[0]
                        new_name = f"{base}.mp4"
                        os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, new_name))
                self.label.text = 'Files renamed to .mp4 successfully'
            except Exception as e:
                self.label.text = f'Error: {e}'
        else:
            self.label.text = 'Directory not found'

    def revert_to_txt(self, instance):
        if not self.directory:
            self.label.text = 'Select a directory first'
            return

        if os.path.exists(self.directory):
            try:
                for filename in os.listdir(self.directory):
                    if filename.endswith('.mp4'):
                        base = os.path.splitext(filename)[0]
                        new_name = f"{base}.txt"
                        os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, new_name))
                self.label.text = 'Files reverted to .txt successfully'
            except Exception as e:
                self.label.text = f'Error: {e}'
        else:
            self.label.text = 'Directory not found'


FileRenameApp().run()
