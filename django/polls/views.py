from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# from django.http import HttpResponse
# from django.template import loader

from polls.models import Question, Choice


def index(request):
    # 가장 최근에 발행된 최대 5개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 쉼표단위로 구분된 Question목록의 각 항목의 question_text로 만들어진 문자
    # output = ', '.join([q.question_text for q in latest_question_list])

    context = {
        'latest_question_list': latest_question_list
    }

    return render(request=request, template_name='polls/index.html', context=context, )

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question
    }

    return render(request=request, template_name='polls/detail.html', context=context, )



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question
    }
    return render(request=request, template_name='polls/results.html', context=context, )




def vote(request, question_id):

    choice_pk = request.POST['choice']
    choice = Choice.objects.get(pk=choice_pk)
    choice.vote +=1
    choice.save()

    return redirect('polls:results', question_id=question_id)
