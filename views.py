from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Submission, Choice, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # الحصول على الاختيارات المختارة من الفورم
        weights = request.POST.getlist('choice')
        # إنشاء سجل تسليم جديد
        # (يفترض وجود سجل Enrollment مسبق للمستخدم الحالي والكورس)
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        
        for choice_id in weights:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
        submission.save()
        
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    total_score = 0
    # حساب النتيجة بناءً على الاختيارات الصحيحة
    for question in course.question_set.all():
        selected_ids = submission.choices.filter(question=question).values_list('id', flat=True)
        if question.is_get_score(selected_ids):
            total_score += question.grade
            
    context = {
        'course': course,
        'submission': submission,
        'total_score': total_score
    }
    return render(request, 'onlinecourse/exam_result.html', context)
