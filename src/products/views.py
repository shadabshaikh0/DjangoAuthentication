from django.views.generic import ListView,DetailView
from django.shortcuts import render
from django.http import Http404

from .models import Product
# Create your views here.

class ProductListView(ListView):
	queryset      = Product.objects.all()
	template_name = "products/list.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id('pk')
		if instance is None:
			raise Http404("Product doesnt exist")
		return instance
	# def get_queryset(self,*args,**kwargs):
	# 	request = self.request
	# 	return Product.objects.all()

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list':queryset	
	}
	return render(request,"products/list.html",context)



class ProductDetailView(DetailView):
	queryset      = Product.objects.all()
	template_name = "products/detail.html"

	def get_contex_data(self,*args,**kwargs):
		context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context

	def get_queryset(self,*args,**kwargs):
		request = self.request
		pk=self.kwargs.get('pk')
		return Product.objects.filter(pk=pk)


def product_detail_view(request,pk=None,*args,**kwargs):
	#instance = get_object_or_404(Product,pk=pk)
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesn't exist")
	# qs = Product.object.filter(id=pk)
	# if qs.exists() and qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("Product doesn't exists ")
	context = {
		'object':instance	
	}
	return render(request,"products/detail.html",context)