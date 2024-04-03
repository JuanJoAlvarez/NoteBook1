from datetime import datetime
from typing import List, Dict

class Note:
    def __init__(self, title: str, text: str, importance: str):
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_time = datetime.now()
        self.tags: List[str] = []

    def __str__(self):
        return f"Code: {id(self)}\nCreation date: {self.creation_time}\n{self.title}: {self.text}"

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

class Notebook:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        note = Note(title, text, importance)
        self.notes.append(note)
        return id(note)

    def list_all_notes(self):
        for note in self.notes:
            print(note)

    def add_tags_to_note(self, code: int, tags: List[str]):
        for note in self.notes:
            if id(note) == code:
                for tag in tags:
                    note.add_tag(tag)

    def list_important_notes(self):
        for note in self.notes:
            if note.importance.upper() in ['HIGH', 'MEDIUM']:
                print(note)

    def delete_note(self, code: int):
        for i, note in enumerate(self.notes):
            if id(note) == code:
                del self.notes[i]
                break

    def tags_note_count(self) -> Dict[str, int]:
        tags_count = {}
        for note in self.notes:
            for tag in note.tags:
                tags_count[tag] = tags_count.get(tag, 0) + 1
        return tags_count

if __name__ == "__main__":
    my_notebook = Notebook()

    # Agregar notas
    code1 = my_notebook.add_note("Título 1", "Texto de la nota 1", "HIGH")
    code2 = my_notebook.add_note("Título 2", "Texto de la nota 2", "MEDIUM")
    code3 = my_notebook.add_note("Título 3", "Texto de la nota 3", "LOW")

    # Agregar etiquetas a notas
    my_notebook.add_tags_to_note(code1, ["tag1", "tag2"])
    my_notebook.add_tags_to_note(code2, ["tag2"])
    my_notebook.add_tags_to_note(code3, ["tag3"])

    # Listar todas las notas
    print("Todas las notas:")
    my_notebook.list_all_notes()
    print()

    # Listar notas importantes
    print("Notas importantes:")
    my_notebook.list_important_notes()
    print()

    # Contador de notas por etiqueta
    print("Contador de notas por etiqueta:")
    tags_count = my_notebook.tags_note_count()
    for tag, count in tags_count.items():
        print(f"{tag}: {count}")
    print()

    # Borrar una nota
    my_notebook.delete_note(code1)

    # Listar notas después de borrar
    print("Notas después de borrar una:")
    my_notebook.list_all_notes()