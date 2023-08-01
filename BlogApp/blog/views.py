from django.shortcuts import render, redirect
from blog.form import BlogForm
from .models import Category, Blog
from blog.serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View


class BlogListCreateAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(homepage=True)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        blog_instance = self.get_object(pk)
        if not blog_instance:
            return Response(
                {
                    'errors': {
                        'code': 404,
                        'message': f'Böyle bir id({pk}) ile ilgili makale bulunamadı.'
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogSerializer(blog_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_instance = self.get_object(pk)
        if not blog_instance:
            return Response(
                {
                    'errors': {
                        'code': 404,
                        'message': f'Böyle bir id({pk}) ile ilgili makale bulunamadı.'
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BlogSerializer(blog_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog_instance = self.get_object(pk)
        if not blog_instance:
            return Response(
                {
                    'errors': {
                        'code': 404,
                        'message': f'Böyle bir id({pk}) ile ilgili makale bulunamadı.'
                    }
                },
                status=status.HTTP_404_NOT_FOUND
            )

        blog_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomeView(View):
    def get(self, request):
        data = {
            "categories": Category.objects.all(),
            "blogs": Blog.objects.filter(homepage=True),
        }
        return render(request, "home.html", data)


class BlogsView(View):
    def get(self, request):
        data = {
            "categories": Category.objects.all(),
            "all_blogs": Blog.objects.all(),
        }
        return render(request, "blog.html", data)


class BlogDetailsView(View):
    def get(self, request, slug):
        data = {
            "blog": Blog.objects.get(slug=slug)
        }
        return render(request, "bdetails.html", data)


class BlogsByCategory(View):
    def get(self, request, slug):
        data = {
            "categories": Category.objects.all(),
            "blogs": Category.objects.get(slug=slug).blog_set.all(),
            "selected_category": slug
        }
        return render(request, "blog.html", data)


class AddBlogView(View):
    def get(self, request):
        form = BlogForm()
        categories = Category.objects.all()
        data = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'addblog.html', data)

    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_name = form.cleaned_data['blog_name']
            desc = form.cleaned_data['desc']
            image = form.cleaned_data['image']
            homepage = form.cleaned_data['homepage']
            categories = form.cleaned_data['categories']
            
            blog = Blog.objects.create(blog_name=blog_name, desc=desc, image=image, homepage=homepage)
            blog.categories.set(categories)
            
            return redirect('home')
        # Form geçersizse tekrar sayfayı göster
        data = {
            'form': form,
            'categories': Category.objects.all(),
        }
        return render(request, 'addblog.html', data)
