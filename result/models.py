from django.db import models
from users.models import Person
import random

class First(models.Model):
    ATTITUDE_CHOICES = [
		('Most times','Most times'),
		('Some times', 'Some times'),
        ('Rarely','Rarely'),
		('Always', 'Always')
	]
    SCHOLASTIC_CHOICES = [
        ('Capable and Competent', 'Capable and Competent'),
		('Experiencing Some Difficulties', 'Experiencing Some Difficulties'),
        ('Experiencing Significant Difficulties', 'Experiencing Significant Difficulties'),
    ]
    session = models.ForeignKey('management.Session', on_delete = models.SET_NULL, default=1, null=True)
    subject = models.ForeignKey('management.Subject', on_delete=models.SET_NULL, null=True, related_name='result_subject')
    student = models.ForeignKey('users.Person', on_delete = models.SET_NULL, null=True)
    school_fees = models.BooleanField(max_length=5, default = False, verbose_name="School Fees")
    value = models.IntegerField(blank=True, default = 0)
    ca1 = models.IntegerField(blank=True, default = 0, verbose_name="1st CA")
    ca2 = models.IntegerField(blank=True, default = 0, verbose_name="2nd CA")
    exam = models.IntegerField(blank=True, default = 0, verbose_name="Exam")
    total = models.IntegerField(blank=True, default = 0)
    subject_total = models.IntegerField(blank=True, default = 0)
    subject_avg = models.FloatField(blank=True, default = 0)
    subject_pos = models.CharField(max_length=5, blank=True, null=True, verbose_name="Subject Position")
    grade = models.CharField(max_length=1, blank=True, null=True)
    cumulative = models.IntegerField(blank=True, default = 0)
    cum_perc = models.FloatField(blank=True, default = 0)
    number_present = models.CharField(max_length=7, blank=True, null=True, verbose_name="No of Days Present")
    concentration = models.CharField(max_length=15, blank=True, choices=ATTITUDE_CHOICES, null=True)
    responsiveness = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, blank=True, null=True)
    comprehension = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, blank=True, null=True)
    interest = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Interest in Learning")
    homework = models.CharField(max_length=15, choices=ATTITUDE_CHOICES, blank=True, null=True, verbose_name="Homework Completion")
    reading = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    writing = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    spoken = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True, verbose_name="Spoken English")
    innovative = models.CharField(max_length=45, choices=SCHOLASTIC_CHOICES, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    static_class = models.CharField(max_length=20, blank=True, null=True)
    static_number = models.CharField(max_length=7, blank=True, null=True)
    static_next = models.DateField(blank=True, null=True)

    def __str__(self):
        try:
            return str(self.student.first_name) + " " + str(self.student.last_name) + " " + str(self.cumulative)
        except:
            return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = "First Term Score"
        verbose_name_plural = "First Term Scores"

    def grade(self):
        if self.total < 50:
            return "E"
        elif self.total >= 50 and self.total < 60:
            return "D"
        elif self.total >= 60 and self.total < 70:
            return "C"
        elif self.total >= 70 and self.total < 85:
            return "B"
        else:
            return "A"

    def grade_general(self):
        if self.cum_perc < 50:
            return "Poor"
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return "Average"
        elif self.cum_perc >= 60 and self.cum_perc < 70:
            return "Good"
        elif self.cum_perc >= 70 and self.cum_perc < 85:
            return "Very Good"
        else:
            return "Excellent"

    def teacher_comment(self):
        if self.student.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.student.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.student.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Dear " + self.student.first_name + "! Your efforts fall short of the required level, try to upgrade your performance next term.",
            "I have truly enjoyed being " + self.student.first_name + "'s teacher and hope for improvement next term.",
            self.student.first_name + " is really trying, but " + pronoun0 + " needs to do more for a better result."]
        choices_60 = [self.student.first_name + ", I believe you can do better than this. We can’t wait for your improvement next term!",
            self.student.first_name + " is a valued member of the class. Significant improvement in " + pronoun + " commitment to studies will make " + pronoun2 + " great.",
            "Great effort, " + self.student.first_name + "! Consistency will make your performance better. I wish you all the best.",
            "Dear " + self.student.first_name + "! Ability to stay on task without distraction will guarantee better result. Hope that would be achieved next term."]
        choices_80 = ["What a great performance from you, " + self.student.first_name + "! You can perform even better next term.",
            self.student.first_name + " has worked very hard this term and I am proud of all of " + pronoun + " accomplishments.",
            self.student.first_name + "'s strength is evident in this result. I look forward for improvement in the weak areas.",
            self.student.first_name + ", you really tried with this result and I commend your attitude to learning. May Allah bless you.",
            "I am so proud of you " + self.student.first_name +  ", and wish you well in your academics subsequent terms."]
        choices_else = ["It is my pleasure being " + self.student.first_name + "'s class teacher for " + pronoun + " zeal to study is on the highest level!",
            self.student.first_name + "'s dedication to study is topnotch! No wonder " + pronoun0 + " has excellent grades throughout.",
            "What an excellent result! " + self.student.first_name + "'s  performance this term is really outstanding!"]

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)

    def head_comment(self):
        if self.student.gender == "FEMALE":
            pronoun0 = "she"
        else:
            pronoun0 = "he"
        if self.student.gender == "FEMALE":
            pronoun = "her"
        else:
            pronoun = "his"
        if self.student.gender == "FEMALE":
            pronoun2 = "her"
        else:
            pronoun2 = "him"
        choices_50 = ["Your performance is not bad, but you need to try harder. May you accomplish that with ease.",
            "You can do better next term; you need to. May Allah make that an easy one for you.",
            "Your performance is not that poor as a fresher. But try to improve your performance next term.",
            "The adventure just begins; nothing to worry about. You will excel in sha Allah."]
        choices_60 = ["I believe you will do better next term. You can, actually. May Allah bless you.",
            "What a good performance! Keep it up. May Allah bless you.",
            "Great effort. I hope to see more next term. May Allah bless you.",
            "What a beginning! I believe the future is promising. May Allah bless you."]
        choices_80 = ["A deserving result for a child who has been wonderful. May Allah bless you.",
            "A praiseworthy performance! You deserve all credits. May Allah bless you.",
            "Such is a result expected from a brilliant scholar like you. I hope to see more of this. May Allah bless you.",
            "This is an excellent performance. Thumbs up. May Allah bless you.",
            "Great performance. This result shows how wonderful you are. May Allah bless you."]
        choices_else = ["A praiseworthy performance! Keep it up. May Allah bless you.",
            "Surely, this is a five-star performance! May Allah bless you.",
            "Maa sha Allah, this is awesome! May Allah bless you.",
            "Maa sha Allah, this is impressive! The sky is surely your starting point. May Allah bless you."]

        if self.cum_perc < 50:
            return random.choice(choices_50)
        elif self.cum_perc >= 50 and self.cum_perc < 60:
            return random.choice(choices_60)
        elif self.cum_perc >= 60 and self.cum_perc < 80:
            return random.choice(choices_80)
        else:
            return random.choice(choices_else)
