from django.shortcuts import render

# Create your views here.
def backtest_home(request):
    return render(request, "backtesthome.html", {})