# Brazil Delivery Time & Revenue Analysis Dashboard

![Dashboard](/Document/delivery%20time%20rev%20by%20location.png)

## 📋 Overview

This is an advanced dual-layer web dashboard that provides comprehensive analysis of both delivery performance and revenue data across Brazilian regions. The dashboard combines delivery time analytics with revenue insights to enable strategic business decision-making.

## 🎯 Key Features

### 1. Dual-Layer Map Visualization
- **🚚 Delivery Time View**: Color-coded circles showing delivery performance
- **💰 Revenue View**: Purple circles with white borders sized by revenue amount
- **🔄 Dual Layer View**: Both metrics simultaneously with distinct visual markers
- **📍 Interactive Map**: Zoom, pan, and hover for detailed region information

### 2. Advanced Filtering System
- **🏛️ State Selector**: Multi-select with dynamic city filtering
- **🏙️ City Selector**: Shows only cities from selected states
- **📦 Delivery Time Slider**: Filter regions by maximum delivery days (1-50 days)
- **🎯 Smart Filters**: All visualizations update in real-time

### 3. Comprehensive Analytics
- **📊 Correlation Analysis**: Scatter plot showing delivery time vs revenue relationship
- **🎯 Performance Matrix**: 2x2 grid identifying business opportunities
- **📈 Distribution Charts**: Histograms and category breakdowns
- **💡 Automated Insights**: Key findings and recommendations

## 🚀 Quick Start

### Method 1: Dual-Layer Dashboard (Recommended)
```bash
cd /Users/fengfeng/Dev/DSAI_M2_Project/olist/notebook
python3 run_visible_test.py
```

### Method 2: Alternative Servers
```bash
# City-enabled dashboard
python3 run_dashboard_with_cities.py

# Basic delivery dashboard  
python3 run_dashboard.py
```

## 📊 Dashboard Components

### Left Control Panel

#### 1. Statistics Summary
- **Total Regions**: Filtered region count
- **Average Delivery Days**: Performance metric
- **Total Revenue**: Combined revenue across regions
- **Average Revenue/Region**: Revenue distribution metric

#### 2. State & City Filters
- **State Selector**: 27 Brazilian states with select all/deselect all
- **Dynamic City Filter**: Shows only cities from selected states (1,647+ cities)
- **Auto-Update**: City list refreshes when states change

#### 3. Delivery Time Controls
- **Time Slider**: Filter by maximum delivery days (1-50 range)
- **Smart Display**: Only visible in delivery and dual views
- **Real-time Updates**: Instant filtering across all visualizations

#### 4. Analysis Insights
- **Automated Analysis**: Key performance insights
- **Revenue Distribution**: Fast vs slow delivery revenue breakdown
- **Business Opportunities**: Identification of improvement areas

### Right Visualization Area

#### 1. Interactive Map 🗺️
- **Three View Modes**:
  - **Delivery View**: Circles colored by delivery speed (green=fast, red=slow)
  - **Revenue View**: Purple circles sized by revenue amount
  - **Dual View**: Both layers with distinct markers and dual color bars
- **Map State Persistence**: Zoom and position maintained when switching views
- **Rich Tooltips**: Detailed information on hover

#### 2. Correlation Analysis 📈
- **Scatter Plot**: Delivery days vs revenue relationship
- **Color Coding**: Points colored by delivery performance
- **Trend Analysis**: Identify correlation patterns
- **Interactive**: Click points for region details

#### 3. Performance Matrix 🎯
- **2x2 Grid**: Fast/Slow delivery vs High/Low revenue
- **Opportunity Identification**: 
  - Fast Delivery + High Revenue: Optimal performance
  - Slow Delivery + High Revenue: Improvement opportunity
  - Fast Delivery + Low Revenue: Growth potential
  - Slow Delivery + Low Revenue: Priority focus areas

## 🎨 Visual Design Features

### Map Visualization
- **Delivery Markers**: Circles with color gradient (green → yellow → red)
- **Revenue Markers**: Purple circles with white borders
- **Size Encoding**: Larger markers indicate higher values
- **Dual Layer**: Offset positioning to show both metrics simultaneously

### Color Schemes
- **Delivery Time**: Green (fast) to Red (slow) gradient
- **Revenue**: Purple gradient (#F3E5F5 to #6A1B9A)
- **UI Theme**: Professional blue gradient theme
- **High Contrast**: White borders for visibility on map backgrounds

### Interactive Elements
- **Smooth Transitions**: Animated view switching
- **Hover Effects**: Enhanced visual feedback
- **Loading States**: Progress indicators during data updates
- **Responsive Design**: Adapts to different screen sizes

## 🔧 Technical Architecture

### Data Integration
- **BigQuery Source**: Real-time data from `fct_delivery_time_by_zip` and `fct_geo_revenue`
- **Dual Data Streams**: Delivery performance + revenue analytics
- **Smart Fallback**: Sample data when BigQuery unavailable
- **JSON Format**: Optimized data structure for web visualization

### Frontend Technologies
- **Plotly.js**: Advanced mapping and charting
- **Vanilla JavaScript**: No framework dependencies
- **CSS3**: Modern styling with gradients and animations
- **HTML5**: Semantic structure with accessibility features

### Performance Optimizations
- **Map State Persistence**: Maintains zoom/position across view switches
- **Real-time Filtering**: Efficient data processing
- **Event-driven Updates**: Only re-render when necessary
- **Responsive Loading**: Progressive data loading

## 📱 Usage Guide

### 1. Basic Navigation
1. **Select States**: Choose regions of interest
2. **Refine Cities**: Fine-tune with city-level selection
3. **Set Time Filter**: Use slider to focus on delivery performance
4. **Switch Views**: Compare delivery vs revenue patterns

### 2. Advanced Analysis
1. **Dual Layer Mode**: View both metrics simultaneously
2. **Correlation Analysis**: Identify delivery-revenue relationships
3. **Performance Matrix**: Find optimization opportunities
4. **Geographic Drilling**: Zoom into specific regions

### 3. Business Insights
- **High Revenue + Slow Delivery**: Priority improvement areas
- **Fast Delivery Regions**: Model for expansion
- **Revenue Concentration**: Identify key markets
- **Performance Gaps**: Strategic investment opportunities

## 📁 File Structure

```
olist/notebook/
├── brazil_delivery_revenue_dashboard.html    # Main dual-layer dashboard
├── brazil_delivery_dashboard_with_cities.html # City-enabled dashboard
├── dashboard_data_generator_en.py            # Data generator with revenue
├── run_visible_test.py                       # Main server script
├── run_dashboard_with_cities.py              # City dashboard server
├── dashboard_data.json                       # Combined delivery + revenue data
└── debug_revenue_map.html                    # Debug/testing page
```

## 🐛 Troubleshooting

### Common Issues

1. **Revenue Markers Not Visible**
   - Ensure using `run_visible_test.py` server
   - Check browser console for JavaScript errors
   - Verify `dashboard_data.json` contains revenue data

2. **City Filter Empty**
   - Select at least one state first
   - Cities auto-populate based on state selection
   - Check data generator includes city information

3. **Map Resets on View Switch**
   - Fixed in latest version with map state persistence
   - Zoom and position maintained across all view modes

4. **Performance Issues**
   - Large datasets may cause slow rendering
   - Use delivery time slider to reduce data volume
   - Consider state/city filtering for better performance

### Data Validation
```bash
# Verify data structure
python3 -c "
import json
with open('dashboard_data.json', 'r') as f:
    data = json.load(f)
print('Keys:', list(data.keys()))
print('Sample record:', list(data['data'][0].keys()))
"
```

## 🔄 Updates and Maintenance

### Data Refresh
```bash
# Update with latest BigQuery data
python3 dashboard_data_generator_en.py
```

### Custom Configuration
- **Revenue Scaling**: Modify marker size calculations
- **Color Schemes**: Adjust gradient definitions
- **Filter Ranges**: Update slider min/max values
- **Map Defaults**: Change initial zoom and center position

## 📊 Business Value

### Strategic Insights
- **Revenue-Performance Correlation**: Understand relationship between delivery speed and revenue
- **Geographic Optimization**: Identify high-value regions for investment
- **Service Level Planning**: Set realistic delivery expectations by region
- **Market Expansion**: Find underserved high-potential areas

### Operational Benefits
- **Performance Monitoring**: Track delivery improvements over time
- **Resource Allocation**: Focus investments on high-impact regions
- **Customer Experience**: Optimize service levels by market
- **Competitive Analysis**: Benchmark performance across regions

---

**Version**: 2.0.0  
**Last Updated**: December 2024  
**Features**: Dual-layer visualization, revenue analytics, dynamic filtering  
**Compatibility**: Modern browsers with JavaScript ES6+ support

## 🌟 Key Improvements from v1.0

- **✅ Dual-Layer Mapping**: Simultaneous delivery and revenue visualization
- **✅ Revenue Analytics**: Complete financial performance integration
- **✅ Dynamic City Filtering**: State-based city selection
- **✅ Delivery Time Slider**: Granular performance filtering
- **✅ Map State Persistence**: Maintains view when switching modes
- **✅ Enhanced Insights**: Automated business intelligence
- **✅ Performance Matrix**: Strategic opportunity identification
- **✅ Correlation Analysis**: Data-driven relationship discovery

The dashboard now provides comprehensive business intelligence for Brazilian logistics operations, combining operational performance with financial outcomes for strategic decision-making.