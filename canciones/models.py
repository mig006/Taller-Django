from django.db import models


GENEROS = [
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('reggaeton', 'Reggaetón'),
    ('hip_hop', 'Hip Hop'),
    ('electronica', 'Electrónica'),
    ('jazz', 'Jazz'),
    ('clasica', 'Clásica'),
    ('salsa', 'Salsa'),
    ('cumbia', 'Cumbia'),
    ('otro', 'Otro'),
]


class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    genero = models.CharField(max_length=20, choices=GENEROS, default='otro')
    duracion_segundos = models.PositiveIntegerField(help_text="Duración en segundos")
    fecha_lanzamiento = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']
        verbose_name_plural = 'canciones'

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

    def duracion_formateada(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{minutos}:{segundos:02d}"
