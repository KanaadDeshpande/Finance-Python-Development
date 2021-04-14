""""This step is the initial base for further steps for creating a diversified portfolio. Created by Kanaad Deshpande"""
def stepOnePartOne(y):
    y = y.strip().split()

    # Scrip is the name of the stock
    Scrip = y[0]
    
    # Share Number is the number of shares that are going to be purchased.
    shareNumber = int(y[1])
    
    # Price per share is the price of individual shares.
    pricePerShare = int(y[2])
    
    # Total investment is the total money invested in the shares
    totalInvestment = shareNumber * pricePerShare
    
    # Target is the target for stock price to attain.
    target = float(y[3])
    
    # Total Target is the total value of the stocks after profit.
    totalTarget = shareNumber * target
    
    # Total profit is, well, the total profit, obviously!
    totalProfit = totalTarget - totalInvestment

    # Profit percent is self-descriptive
    profitPercent = (totalProfit / totalInvestment) * 100

    # Risk Taking Ability is the ability of the investor to take risks.
    riskTakingAbility = float(y[4])
    
    return Scrip, shareNumber, pricePerShare, totalInvestment, target, totalTarget, totalProfit, profitPercent, riskTakingAbility

def stepOnePartTwo(y):
    Scrip, shareNumber, pricePerShare, totalInvestment, target, totalTarget, totalProfit, profitPercent, riskTakingAbility = stepOnePartOne(y)    

    # Loss is the loss that the investor might have to deal with
    loss = (totalInvestment * riskTakingAbility)/100

    # Stop loss is the price below which the investor will not allow the share price to fall. 
    # If it does, the shares will be sold.
    stopLoss = pricePerShare - loss/shareNumber

    # Profits you gain per unit of risk taken is the risk:return ratio.
    riskToReturnRatio = "1" + ":" + str(totalProfit/loss) 
    return Scrip, riskTakingAbility, stopLoss, loss, riskToReturnRatio

def printingFunctionForStepOnePartOne(y):
    """This function prints all the variables of the function stepOnePartOne"""
    Scrip, shareNumber, pricePerShare, totalInvestment, target, totalTarget, totalProfit, profitPercent, riskTakingAbility = stepOnePartOne(y)
    return f'{Scrip}\t\t{shareNumber}\t\t\t{pricePerShare}\t\t\t{totalInvestment}\t\t\t{target}\t\t\t{totalTarget}\t\t\t{totalProfit}\t\t\t{profitPercent}'

def printingFunctionForStepOnePartTwo(y):
    """This function prints all the variables of the function stepOnePartTwo"""
    Scrip, riskTakingAbility, stopLoss, loss, riskToReturnRatio = stepOnePartTwo(y)
    return f'{Scrip}\t\t{riskTakingAbility}\t\t{stopLoss}\t\t{loss}\t\t{riskToReturnRatio}'

if __name__ == '__main__':
    print("******************")
    print("Create a portfolio")
    print("******************")
    x = int(input("Enter the number of companies: "))  
    a = []  
    print("Enter the Scrip, number of shares, price per share, and risk taking ability:")
    for i in range(x):
        y = input()
        a.append(y)

    print("\n")
    listToBePrintedForStepOne = "Scrip|\tNumber of shares|\tPrice Per Share|\tTotal Amount Invested|\tTarget Price per share|\t\tTotal target|\t\tTotal profit|\t\tTotal profit %|"
    print(listToBePrintedForStepOne)
    for j in range(len(a)):
        print(printingFunctionForStepOnePartOne(a[j]))

    print("\n")
    listToBePrintedForStepTwo = "Scrip|\tRisk Taking Ability|\tStop Loss|\tLoss|\t\tRisk:Return|"
    print(listToBePrintedForStepTwo)
    for k in range(len(a)):
        print(printingFunctionForStepOnePartTwo(a[k]))       