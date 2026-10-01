import pandas as pd
from src.plot_polar import plot_polar

# Example dataset
df = pd.DataFrame({
"country": [
"Italy",
"France",
"Spain",
"Germany",
"Portugal",
"Greece"
],
"score": [
82,
76,
91,
88,
79,
85
]
})

# Create the polar chart
figure = plot_polar(
  df,
  category_column="country",
  value_column="score",
  color_map="viridis",
  title="Country Scores"
)

# The DataIndy platform handles the returned Figure.
