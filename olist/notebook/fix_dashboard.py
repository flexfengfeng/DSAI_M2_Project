#!/usr/bin/env python3
"""
Fix the dashboard by adding debug info and ensuring JSON loads properly
"""

# Read the original dashboard
with open('brazil_delivery_dashboard_en.html', 'r') as f:
    content = f.read()

# Add debug logging to the loadData function
old_load_function = '''        async function loadData() {
            try {
                // Try to load real data
                const response = await fetch('dashboard_data.json');
                if (response.ok) {
                    const data = await response.json();
                    rawData = data.data;
                    dashboardStats = data.stats;
                    updateLastUpdateTime(data.stats.last_updated);
                } else {
                    throw new Error('Unable to load data file');
                }
            } catch (error) {
                console.log('Using sample data:', error.message);
                rawData = generateSampleData();
                dashboardStats = calculateStats(rawData);
                updateLastUpdateTime();
            }
            
            initializeFilters();
            updateDashboard();
        }'''

new_load_function = '''        async function loadData() {
            try {
                // Try to load real data
                console.log('🔄 Attempting to load dashboard_data.json...');
                const response = await fetch('dashboard_data.json');
                console.log('📡 Response status:', response.status);
                
                if (response.ok) {
                    const data = await response.json();
                    rawData = data.data;
                    dashboardStats = data.stats;
                    updateLastUpdateTime(data.stats.last_updated);
                    console.log('✅ JSON data loaded successfully!');
                    console.log('📊 Records loaded:', rawData.length);
                    console.log('📈 JSON avg:', dashboardStats.avg_delivery_days);
                    
                    // Add visual indicator
                    document.title = '✅ Dashboard (Real Data - ' + dashboardStats.avg_delivery_days + ' days avg)';
                } else {
                    throw new Error('Unable to load data file - HTTP ' + response.status);
                }
            } catch (error) {
                console.log('❌ Error loading JSON:', error.message);
                console.log('🔄 Using sample data fallback...');
                rawData = generateSampleData();
                dashboardStats = calculateStats(rawData);
                updateLastUpdateTime();
                
                // Add visual indicator
                const sampleAvg = rawData.reduce((sum, d) => sum + d.avg_delivery_days, 0) / rawData.length;
                document.title = '⚠️ Dashboard (Sample Data - ' + sampleAvg.toFixed(1) + ' days avg)';
            }
            
            initializeFilters();
            updateDashboard();
        }'''

# Replace the function
content = content.replace(old_load_function, new_load_function)

# Write the fixed dashboard
with open('brazil_delivery_dashboard_fixed.html', 'w') as f:
    f.write(content)

print("✅ Created brazil_delivery_dashboard_fixed.html with debug logging")
print("🔍 Check browser console and page title to see if JSON loads")