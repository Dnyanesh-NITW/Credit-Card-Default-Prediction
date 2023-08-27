# Credit-Card-Default-Prediction

## Overview
This project presents a classification model designed to predict credit card defaulters using a commonly encountered dataset. The aim is to predict potential credit card defaulters for the next month based on customer demographic information and their behavior over the past six months.

## Inspiration
Credit card debt can quickly spiral out of control due to factors like job loss, medical emergencies, or business failures. Even seemingly manageable debts can become unmanageable due to compounding finance charges and penalties. This project addresses the challenge of predicting if a customer will default on their credit card payments in the coming months.

## How does a credit card system works?

* Every month, you receive a bill (X) reflecting your credit card expenses.
* You make a payment (Y), typically the minimum amount due, by the due date mentioned on the billing statement
* The next month's bill includes the remaining balance from the previous month (X - Y) plus any new expenses (X') incurred during that month.
* You make another payment (Y') to cover part of the new bill.
* This cycle repeats, with each month's bill incorporating previous balances, new expenses, and subtracting payments.

Missing the minimum payment due date leads to a late payment, often accompanied by late fees. In addition, continued delay might lead to default

## Dataset Information
The dataset contains 30000 credit card clients data on default payments, demographic factors, credit history, payment behavior, and billing statements of credit card clients in Taiwan from April 2005 to September 2005.

There are 25 variables:

- **ID**: ID of each client
- **LIMIT_BAL**: Amount of given credit in NT dollars (includes individual and family/supplementary credit)
- **SEX**: Gender (1=male, 2=female)
- **EDUCATION**: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
- **MARRIAGE**: Marital status (1=married, 2=single, 3=others)
- **AGE**: Age in years
- **PAY_0**: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
- **PAY_2**: Repayment status in August, 2005 (scale same as above)
- **PAY_3**: Repayment status in July, 2005 (scale same as above)
- **PAY_4**: Repayment status in June, 2005 (scale same as above)
- **PAY_5**: Repayment status in May, 2005 (scale same as above)
- **PAY_6**: Repayment status in April, 2005 (scale same as above)
- **BILL_AMT1**: Amount of bill statement in September, 2005 (NT dollar)
- **BILL_AMT2**: Amount of bill statement in August, 2005 (NT dollar)
- **BILL_AMT3**: Amount of bill statement in July, 2005 (NT dollar)
- **BILL_AMT4**: Amount of bill statement in June, 2005 (NT dollar)
- **BILL_AMT5**: Amount of bill statement in May, 2005 (NT dollar)
- **BILL_AMT6**: Amount of bill statement in April, 2005 (NT dollar)
- **PAY_AMT1**: Amount of previous payment in September, 2005 (NT dollar)
- **PAY_AMT2**: Amount of previous payment in August, 2005 (NT dollar)
- **PAY_AMT3**: Amount of previous payment in July, 2005 (NT dollar)
- **PAY_AMT4**: Amount of previous payment in June, 2005 (NT dollar)
- **PAY_AMT5**: Amount of previous payment in May, 2005 (NT dollar)
- **PAY_AMT6**: Amount of previous payment in April, 2005 (NT dollar)
- **default.payment.next.month**: Default payment (1=yes, 0=no)

## Technologies Used

![WhatsApp Image 2023-08-27 at 4 05 06 PM](https://github.com/Dnyanesh-NITW/Credit-Card-Default-Prediction/assets/136236322/95a9f629-17bc-4e55-adfb-b7b3ec083ed6)

## Analysis Conclusions

The following insights shed light on how different columns in the dataset relate to the default column
 
**Repayment Behavior**:
Individuals with a history of payment delays for more than 4 months have a significantly high chance of default, approximately 70%.

**Bill Statement**:
Individuals with negative bill statements (credit balance) are less likely to default

**Previous Payment Amounts**:
Individuals with very low previous payment amounts, nearly 0, have a higher likelihood of default, around 30%.

**Education Level**:
As the education level decreases, the limit balance also decreases, and the chance of default increases

**Marital Status**:
Individuals with marital status "Others" (possibly divorced) have a notably higher chance of default, approximately 30

**Age Group**:
People belonging to the age group of 20 to 25 and above 50 have a higher likelihood of default, around 27%.

**Credit Limit**:
Individuals with higher credit limits are less prone to default, while those with credit limits below 50k dollars have a high likelihood of default, almost 32%

## Demo Video

https://github.com/Dnyanesh-NITW/Credit-Card-Default-Prediction/assets/136236322/563e1fdd-29c1-4e11-bd8f-2722dc208a57


<p align="center">
  <span style="font-size: 36px; font-weight: bold;">🙏 Thank You! 🙏</span>
</p>

<p align="center">
  If you find this project helpful, please consider giving it a ⭐️!
</p>
