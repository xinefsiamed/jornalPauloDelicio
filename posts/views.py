from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post
from django.db.models import Q
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages
from .forms import FormPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from categorias.models import Categoria

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        qs = qs.filter(
            publicado_post = True,
        )

        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()

        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/categoria_post.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario

    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()

        comentarios = Comentario.objects.filter(
            publicado_comentario=True,
            post_comentario=post.id
        )

        contexto['comentarios'] = comentarios

        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        comentario.save()
        messages.success(self.request, 'Comentario enviado para revisão')
        return redirect('post_detalhes', pk=post.id)


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class Escrever(StaffRequiredMixin, CreateView):
    template_name = 'posts/criar_post.html'
    model = Post
    form_class = FormPost
    

    def form_valid(self, form):
        print(self.request.user.is_staff)
        post = Post(autor_post_id=self.request.user.id, **form.cleaned_data)

        post.save()

        return redirect('index')    

    

    