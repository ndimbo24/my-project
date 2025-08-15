# loanapp/views.py
from django.shortcuts import render
from .utils import load_model

model = load_model()

def predict_loan(request):
    result = None
    reasoning = None
    if request.method == 'POST':
        try:
            features = [
                float(request.POST['ApplicantIncome']),
                float(request.POST['CoapplicantIncome']),
                float(request.POST['LoanAmount']),
                float(request.POST['Gender_Male']),
                float(request.POST['Married_Yes']),
                float(request.POST['Dependents_1']),
                float(request.POST['Self_Employed_Yes']),
                float(request.POST['Property_Area_Semiurban'])
            ]
            prediction = model.predict([features])[0]

            if prediction == 1:
                result = "Active"
                reasoning = "The applicant's financial profile and property details indicate the loan is likely active."
            else:
                result = "Inactive"
                reasoning = "The provided loan details match profiles where loans are not active."

        except Exception as e:
            result = "Error"
            reasoning = str(e)

    return render(request, "loanapp/loan_form.html", {"result": result, "reasoning": reasoning})
