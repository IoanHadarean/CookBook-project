import pygal
from app.models import values
from app.models.values import French_val, Mexican_val, Greek_val, English_val
from app.models.values import Asian_val, Indian_val, Irish_val, Italian_val

""" Recipe Graphs class used for the statistics in the routes """


class Graphs:
    
    """ Recipe ingredients statistics by cuisine """
    
    @staticmethod
    def dot_chart():

        dot_chart = pygal.Dot(x_label_rotation=30, print_values=False,
                              show_legend=False,
                              style=pygal.style.styles['default']
                              (value_font_size=30,
                              title_font_size=30,
                              legend_font_size=30,
                              dots_size=3000,
                              background='transparent',
                              tooltip_font_size=30,
                              label_font_size=22))
        dot_chart.title = 'Recipe Ingredients Statistics by Cuisine'
        dot_chart.y_title = 'Recipes by cuisine'
        dot_chart.x_labels = ['milk', 'egg', 'sugar',
                              'flour', 'salt', 'water',
                              'garlic', 'vanilla', 'butter']
        dot_chart.y_labels = ['French - 4', 'Mexican - 2', 'Greek - 2',
                              'English - 2', 'Asian - 4', 'Indian - 3',
                              'Irish - 2', 'Italian - 5']
        dot_chart.add('French', French_val)
        dot_chart.add('Mexican', Mexican_val)
        dot_chart.add('Greek', Greek_val)
        dot_chart.add('English', English_val)
        dot_chart.add('Asian', Asian_val)
        dot_chart.add('Indian', Indian_val)
        dot_chart.add('Irish', Irish_val)
        dot_chart.add('Italian', Italian_val)
        dot_chart = dot_chart.render_data_uri()
        
        return dot_chart
    
    """ Recipe allergens statistics (in %) """
    
    @staticmethod
    def solid_gauge_chart():

        solid_gauge_chart = pygal.SolidGauge(inner_radius=0.70,
                                             style=pygal.style.styles['default']
                                             (value_font_size=25,
                                             title_font_size=30,
                                             legend_font_size=30,
                                             background='transparent',
                                             tooltip_font_size=30))
        solid_gauge_chart.title = 'Recipe Allergens Statistics (in %)'
        percent_formatter = lambda x: '{:.10g}%'.format(x)
        solid_gauge_chart.value_formatter = percent_formatter

        solid_gauge_chart.add('Egg', [{'value': 37.5, 'max_value': 100}])
        solid_gauge_chart.add('Milk', [{'value': 8.33, 'max_value': 100}])
        solid_gauge_chart.add('Nuts', [{'value': 4.16, 'max_value': 100}])
        solid_gauge_chart.add('Garlic', [{'value': 41.66, 'max_value': 100}])
        solid_gauge_chart.add('No allergens', [{'value': 25, 'max_value': 100}])
        solid_gauge_chart = solid_gauge_chart.render_data_uri()
        
        return solid_gauge_chart
    
    
    """ Average calories by cuisine """  
    
    @staticmethod
    def gauge_chart():


        gauge_chart = pygal.Gauge(human_readable=True,
                                  style=pygal.style.styles['default']
                                  (value_font_size=30, title_font_size=30,
                                  legend_font_size=30, background='transparent',
                                  tooltip_font_size=30, label_font_size=25))
        gauge_chart.title = 'Average calories by cuisine'
        gauge_chart.range = [0, 1000]
        gauge_chart.add('French', 393.5)
        gauge_chart.add('Mexican', 296)
        gauge_chart.add('Greek', 599)
        gauge_chart.add('English', 476)
        gauge_chart.add('Asian', 292)
        gauge_chart.add('Indian', 204.66)
        gauge_chart.add('Irish', 413.5)
        gauge_chart.add('All', 344.91)
        gauge_chart = gauge_chart.render_data_uri()
        
        return gauge_chart