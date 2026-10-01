import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from src.plot_polar import plot_polar




def test_plot_polar_returns_figure():
  df = pd.DataFrame({
  "country": ["Italy", "France", "Spain", "Germany"],
  "score": [80, 75, 90, 85]
  })
  
  result = plot_polar(
      df,
      category_column="country",
      value_column="score"
  )

  assert isinstance(result, matplotlib.figure.Figure)
  
  plt.close(result)




def test_plot_polar_invalid_category_column():
  df = pd.DataFrame({
  "country": ["Italy", "France"],
  "score": [80, 75]
  })


  result = plot_polar(
      df,
      category_column="invalid",
      value_column="score"
  )

  assert "valid 'category_column'" in result["message"]




def test_plot_polar_invalid_value_column():
  df = pd.DataFrame({
  "country": ["Italy", "France"],
  "score": [80, 75]
  })


  result = plot_polar(
      df,
      category_column="country",
      value_column="invalid"
  )

  assert "valid 'value_column'" in result["message"]




def test_plot_polar_non_numeric_value():
  df = pd.DataFrame({
  "country": ["Italy", "France"],
  "score": ["high", "low"]
  })


  result = plot_polar(
      df,
      category_column="country",
      value_column="score"
  )

  assert "must be numerical" in result["message"]




def test_plot_polar_same_columns():
  df = pd.DataFrame({
  "score": [80, 75, 90]
  })

  result = plot_polar(
      df,
      category_column="score",
      value_column="score"
  )

  assert "must be different" in result["message"]




def test_plot_polar_invalid_color_map():
  df = pd.DataFrame({
  "country": ["Italy", "France"],
  "score": [80, 75]
  })
  
  result = plot_polar(
      df,
      category_column="country",
      value_column="score",
      color_map="not_a_real_color_map"
  )

  assert "was not found" in result["message"]




def test_plot_polar_missing_values():
  df = pd.DataFrame({
  "country": ["Italy", "France", None, "Germany"],
  "score": [80, 75, 90, None]
  })

  result = plot_polar(
      df,
      category_column="country",
      value_column="score"
  )

  assert isinstance(result, matplotlib.figure.Figure)

  plt.close(result)




def test_plot_polar_too_few_rows():
  df = pd.DataFrame({
  "country": ["Italy"],
  "score": [80]
  })
  
  result = plot_polar(
      df,
      category_column="country",
      value_column="score"
  )
  
  assert "At least two usable rows" in result["message"]




def test_plot_polar_custom_title():
  df = pd.DataFrame({
  "country": ["Italy", "France", "Spain"],
  "score": [80, 75, 90]
  })
  
  result = plot_polar(
      df,
      category_column="country",
      value_column="score",
      title="Country Scores"
  )
  
  assert isinstance(result, matplotlib.figure.Figure)
  assert result.axes[0].get_title() == "Country Scores"
  
  plt.close(result)

