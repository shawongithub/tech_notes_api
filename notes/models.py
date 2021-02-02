from django.db import models

class Notes(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=264, verbose_name="Put a Title")
    body = models.TextField()
    shared = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date', ]

    def __str__(self):
        return self.title

class SharedNotes(models.Model):
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name="shared_notes")
    viewer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="shared_viewer")
    def __str__(self):
        return self.notes.title
