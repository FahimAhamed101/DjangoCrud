from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import  Tasks,FeedFile
from django.urls import reverse_lazy
from .forms import TaskForm,FileModelForm
# Create your views here.
class ListTasks(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = "task_list.html"
    

class DetailTask(DetailView):
    
    template_name = "task_detail.html"
    model = Tasks
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks:pk')
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Tasks.objects.get(pk=pk)
        if instance is None:
            raise Http404("tasks not exists")
        return instance
    
class CreatTask(CreateView):
    
    success_url = reverse_lazy('tasks:tasks')
    template_name = "tasks_creation.html"
    form_class = TaskForm
    
    def form_valid(self, form):
        user = self.request.user
        if self.request.method == 'POST':
            form = TaskForm(self.request.POST)
            file_form = FileModelForm(self.request.POST, self.request.FILES)
            files = self.request.FILES.getlist('images')
            print(files)
            #field name in model
            if form.is_valid() and file_form.is_valid():
                task_instance = form.save(commit=False)
                #task_instance.user = user
                task_instance.save()
                for f in files:
                    file_instance = FeedFile(image=f, tasks=task_instance)
                    file_instance.save()
        else:
            form = TaskForm()
            file_form = FileModelForm()

        return super(CreatTask, self).form_valid(form)          
    
    
    
class EditTask(UpdateView,):
    
    model = Tasks
    form_class = TaskForm
    success_url = reverse_lazy('tasks:tasks')
    template_name = "task_update.html"
    
    def get_queryset(self,**kwarg):
        pk = self.kwargs.get('pk')
        instance = Tasks.objects.all().filter(pk=pk)
        print(instance)
        
        if instance is None:
            raise Http404("tasks not exists")
        return instance
    
    def form_valid(self, form):
        user = self.request.user
        if self.request.method == 'POST':
            pk = self.kwargs.get('pk')
            instance = Tasks.objects.all().filter(pk=pk)
            instance.delete()
            form = TaskForm(self.request.POST)
            file_form = FileModelForm(self.request.POST, self.request.FILES)
            files = self.request.FILES.getlist('images')
            print(files)
            #field name in model
            if form.is_valid() and file_form.is_valid():
                task_instance = form.save(commit=False)
                #task_instance.user = user
                task_instance.save()
                for f in files:
                    file_instance = FeedFile(image=f, tasks=task_instance)
                    
                    file_instance.save()
        else:
            form = TaskForm()
            file_form = FileModelForm()

        return super(EditTask, self).form_valid(form) 
  
    

class DeleteTask(DeleteView):
    model = Tasks
    template_name = "task_delete.html"
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks:tasks')
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        task = Tasks.objects.all().filter(completed=False)
        task_count = task.count()
        context['task_count'] = task_count
        return context