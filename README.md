# Brazil Regional Average Delivery Time Analysis Dashboard

![Dashboard](/Document/delivery%20time%20by%20location.png)

![Dashboard](/Document/revenue%20by%20location.png)

## 📋 Overview

This is an integrated web dashboard that consolidates the previously scattered Jupyter notebook outputs into a unified web interface, providing intuitive data visualization and interactive functionality.

## 🎯 Key Improvements

### 1. Unified Layout Design
- **Left Panel**: Filters and data summary
- **Right Top**: Interactive map
- **Right Bottom**: Three side-by-side analysis charts

### 2. Enhanced User Experience
- Responsive design for different screen sizes
- Modern UI design with smooth animations
- Intuitive interactive controls and feedback

### 3. Enhanced Features
- Real-time data filtering and updates
- Select All/Deselect All shortcuts
- Slider control for minimum order count
- Hover tooltips with detailed information

## 🚀 Quick Start

### Method 1: Using Startup Script (Recommended)
```bash
cd ~/olist/notebook
python start_dashboard_en.py
```

### Method 2: Manual Start
```bash
cd ~/olist/notebook
python -m http.server 8000
# Then visit: http://localhost:8000/brazil_delivery_dashboard_en.html
```

## 📊 Dashboard Components

### Left Filter Panel

#### 1. Data Summary Cards
- **Regions**: Total number of regions under current filter
- **States**: Number of states involved
- **Avg Delivery Days**: Average across all regions
- **Total Orders**: Total order volume

#### 2. State Selector
- Multi-select checkboxes for states to display
- Supports Select All/Deselect All operations
- Real-time map and chart updates

#### 3. Delivery Time Category Filter
- Filter by delivery speed categories: Fast, Medium, Slow, Very Slow
- Supports multi-select and select all operations

#### 4. Minimum Order Count Slider
- Drag slider to set minimum order count threshold
- Filters out regions with low order volumes

### Right Content Area

#### 1. Interactive Map 🗺️
- **Dot Size**: Represents average delivery time (larger = slower)
- **Color Gradient**: Green (fast) → Red (slow)
- **Interactive Features**: Zoom, pan, hover for details
- **Geographic Coverage**: Entire Brazil region

#### 2. Average Delivery Days by State Bar Chart 📊
- X-axis: State codes
- Y-axis: Average delivery days
- Color: Based on delivery time
- Shows specific values

#### 3. Delivery Time Category Pie Chart 🥧
- Donut chart showing category percentages
- Color coding: Green (Fast) to Red (Very Slow)
- Shows percentages and labels

#### 4. Delivery Days Distribution Histogram 📈
- Shows frequency distribution of delivery days
- Helps identify data distribution patterns
- X-axis: Delivery days, Y-axis: Frequency

## 🎨 Design Features

### Visual Design
- **Color Scheme**: Blue theme, professional and modern
- **Gradient Effects**: Header and buttons use gradient backgrounds
- **Shadow Effects**: Cards and panels have depth
- **Animation Interactions**: Smooth transitions on hover and click

### Responsive Layout
- **Desktop**: Left-right split layout
- **Tablet**: Adaptive adjustments
- **Mobile**: Vertical stacked layout

## 📱 Usage Tips

### 1. Data Filtering
- First select states of interest
- Then choose delivery time categories
- Finally adjust minimum order count threshold

### 2. Map Operations
- Mouse wheel to zoom for details
- Drag to move view
- Click dots for detailed information

### 3. Chart Interactions
- Hover to see specific values
- Charts update in real-time based on filter conditions

### 4. Data Refresh
- Click "Refresh Data" button to get latest data
- System shows loading status

## 🔧 Technical Architecture

### Frontend Technologies
- **HTML5**: Semantic structure
- **CSS3**: Modern styles and animations
- **JavaScript ES6+**: Interactive logic
- **Plotly.js**: Chart rendering

### Data Processing
- **Python**: Backend data processing
- **BigQuery**: Data source
- **JSON**: Data exchange format

### Deployment
- **Static Files**: Pure frontend implementation
- **HTTP Server**: Python built-in server
- **Local Deployment**: No external dependencies

## 📁 File Structure

```
notebook/
├── brazil_delivery_dashboard_en.html    # Main dashboard file
├── dashboard_data_generator_en.py       # Data generator (English)
├── start_dashboard_en.py               # Startup script (English)
├── dashboard_data.json                 # Data file
├── README_Dashboard_EN.md              # This documentation
└── geo_delivery_dashboard2.ipynb      # Original notebook
```

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Modify port number in startup script
   - Or terminate process using the port

2. **Data Loading Failed**
   - Check if dashboard_data.json file exists
   - Run data generator to recreate data

3. **Charts Not Displaying**
   - Check network connection (needs to load Plotly.js)
   - Ensure browser supports modern JavaScript

4. **BigQuery Connection Issues**
   - Check Google Cloud authentication
   - System will automatically use sample data as fallback

### Browser Compatibility
- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## 🔄 Updates and Maintenance

### Data Updates
```bash
python dashboard_data_generator_en.py
```

### Custom Configuration
- Modify data generator query statements
- Adjust HTML styles and layout
- Change chart color schemes

## 📞 Support

For issues or suggestions:
1. Check the troubleshooting section in this document
2. Review browser console error messages
3. Contact the development team

---

**Version**: 1.0.0  
**Last Updated**: December 2024  
**Compatibility**: Modern browsers

## 🌟 Key Features Summary

- **Interactive Map**: Visual representation of delivery times across Brazil
- **Real-time Filtering**: Dynamic updates based on user selections
- **Multiple Chart Types**: Bar chart, pie chart, and histogram
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Professional UI**: Modern design with smooth animations
- **Easy Deployment**: Simple Python-based local server
- **Data Integration**: Connects to BigQuery with fallback sample data

The dashboard transforms complex delivery data into an intuitive, interactive experience for English-speaking users analyzing Brazilian logistics patterns.
