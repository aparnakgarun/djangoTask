from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from .forms import PortfolioForm

@login_required
def portfolio_view(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    return render(request, 'portfolio/portfolio.html', {'portfolio': portfolio})

@login_required
def edit_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_view')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/edit_portfolio.html', {'form': form})
