def my_graph():
    adj_list = {
        "A" : ["B", "C"],
        "B" : ["A", "D"],
        "C" : ["A", "D", "E"],
        "D" : ["B", "C", "E"],
        "E" : ["C", "D"]
    }
    print(adj_list["B"])
    
