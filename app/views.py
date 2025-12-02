from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Amp, Fuzz, Guitar


def index(request):
    return render(request, 'index.html')


def guitar_detail(request, pk):
    """Display detailed information about a specific guitar."""
    guitar = get_object_or_404(Guitar, pk=pk)
    return render(request, 'product_detail.html', {
        'product': guitar,
        'product_type': 'guitar',
        'product_type_display': 'Đàn Guitar',
    })


def amp_detail(request, pk):
    """Display detailed information about a specific amplifier."""
    amp = get_object_or_404(Amp, pk=pk)
    return render(request, 'product_detail.html', {
        'product': amp,
        'product_type': 'amp',
        'product_type_display': 'Loa & Ampli',
    })


def fuzz_detail(request, pk):
    """Display detailed information about a specific fuzz pedal."""
    fuzz = get_object_or_404(Fuzz, pk=pk)
    return render(request, 'product_detail.html', {
        'product': fuzz,
        'product_type': 'fuzz',
        'product_type_display': 'Fuzz Pedal',
    })


def search(request):
    """Search view that searches across Guitar, Amp, and Fuzz models."""
    query = request.GET.get('q', '').strip()
    
    guitars = []
    amps = []
    fuzzes = []
    
    if query:
        # Search in Guitar model
        guitars = Guitar.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query) |
            Q(body_type__icontains=query) |
            Q(pickup_configuration__icontains=query)
        )
        
        # Search in Amp model
        amps = Amp.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query) |
            Q(amp_type__icontains=query)
        )
        
        # Search in Fuzz model
        fuzzes = Fuzz.objects.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query) |
            Q(description__icontains=query) |
            Q(fuzz_type__icontains=query)
        )
    
    # Calculate total results using count() for better performance
    total_results = guitars.count() + amps.count() + fuzzes.count() if query else 0
    
    context = {
        'query': query,
        'guitars': guitars,
        'amps': amps,
        'fuzzes': fuzzes,
        'total_results': total_results,
    }
    
    return render(request, 'search.html', context)