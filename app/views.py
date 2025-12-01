from django.db.models import Q
from django.shortcuts import render

from .models import Amp, Fuzz, Guitar


def index(request):
    return render(request, 'index.html')


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