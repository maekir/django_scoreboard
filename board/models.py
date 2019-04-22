from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User

class Racer(models.Model):
    """Model representing a racer"""
    # PK
    id = models.UUIDField('Identifier', primary_key=True, default=uuid.uuid4, editable=False)
    # name of racer
    name_r = models.CharField('Name', max_length=200, help_text='Enter the racer\'s name')
    # name of team
    name_t = models.CharField('Team', max_length=200, help_text='Enter the team\'s name')
    # description of car
    desc_c = models.CharField('Car', max_length=1000, help_text='Enter the car\'s description')
    # description of racer
    desc_r = models.CharField('Description', max_length=1000, help_text='Enter the racer\'s description')

    EXP_RACER = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('E', 'Experienced'),
        ('P', 'Professional'),
    )

    # experience of racer
    exp_r = models.CharField(
        'Experience',
        max_length=1,
        choices=EXP_RACER,
        blank=False,
        default='B',
        help_text='Choose the racer\'s experience'
    )

    CLASS_RACER = (
        ('4', 'Fourth'),
        ('3', 'Third'),
        ('2', 'Second'),
        ('1', 'First'),
    )
    
    # class of racer
    class_r = models.CharField(
        'Class',
        max_length=1,
        choices=CLASS_RACER,
        blank=False,
        default='4',
        help_text='Choose the racer\'s class'
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name_r


class Race(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    first = models.ForeignKey('Racer', related_name='racer_first', on_delete=models.SET_NULL, null=True) 
    second = models.ForeignKey('Racer', related_name='racer_second', on_delete=models.SET_NULL, null=True) 
    third = models.ForeignKey('Racer', related_name='racer_third', on_delete=models.SET_NULL, null=True) 
    fourth = models.ForeignKey('Racer', related_name='racer_fourth', on_delete=models.SET_NULL, null=True) 
    fifth = models.ForeignKey('Racer', related_name='racer_fifth', on_delete=models.SET_NULL, null=True) 
    
    def get_absolute_url(self):
        return reverse('race-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commenter = models.ForeignKey(User, verbose_name='commenter', related_name='commenter_id', on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(Race, verbose_name='race', related_name='race_id', on_delete=models.SET_NULL, null=True) 
    text = models.CharField('Text', max_length=3000, help_text='Enter comment text')
    COMMENT_TYPE = (
        ('0', 'Other'),
        ('1', 'Question about the race'),
        ('2', 'Collaboration inquiry')
    )
    type = models.CharField(
        'Type',
        max_length=1,
        choices=COMMENT_TYPE,
        blank=False,
        default='0',
    )
    def __str__(self):
        return f'{self.id} ({self.race})'

