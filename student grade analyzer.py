def analyze_scores(scores):
    average = sum(scores) / len(scores)
    passed = 0
    for score in scores:
        if score >= 50:
            passed += 1
            
    highest = max(scores)
    lowest = min (scores)
            
            
    return average , passed, highest, lowest  
scores = [45, 60, 72, 30, 90, 55]
result = analyze_scores(scores)
print(result)      

