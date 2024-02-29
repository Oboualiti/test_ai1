from django.shortcuts import render
from diffusers import DiffusionPipeline
import torch

# Create your views here.
def index(request):
    return render(request , 'index.html')

def result_template(request):
    return render(request , 'result_template.html')
def input_form(request):
    return render(request , 'input_form.html')

def my_view(request):
    
    
    if request.method == 'POST':
        
        prompt = request.POST.get('prompt', '')  # Assuming you have a form field named 'prompt'
        pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
        pipe.to("cuda")
        images = pipe(prompt=prompt).images[0]

        # Now you have 'images' variable containing the processed images, you can pass it to your template or do whatever you want with it
        return render(request, 'result_template.html', {'images': images})
    else:
        return render(request, 'input_form.html')