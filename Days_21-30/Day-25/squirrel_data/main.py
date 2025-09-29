import pandas

squirrel_data=pandas.read_csv("squirrel_data.csv")

# Count squirrels by fur color
fur_color_counts = squirrel_data["Primary Fur Color"].value_counts()
fur_color_counts.to_csv("squirrel_count.csv")





