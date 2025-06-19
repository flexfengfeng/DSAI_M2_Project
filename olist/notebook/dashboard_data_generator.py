#!/usr/bin/env python3
"""
巴西送货时间仪表盘数据生成器
从BigQuery获取数据并生成JSON文件供HTML仪表盘使用
"""

import pandas as pd
import json
import datetime
from google.cloud import bigquery
import os

class DeliveryDashboardDataGenerator:
    def __init__(self, project_id="brazil-olist"):
        self.project_id = project_id
        self.client = bigquery.Client(project=project_id)
        
    def fetch_delivery_data(self):
        """从BigQuery获取送货时间数据"""
        print("正在从BigQuery加载数据...")
        
        query = f"""
        SELECT 
            zip_code_prefix,
            avg_latitude,
            avg_longitude,
            city,
            state,
            avg_delivery_days,
            delivery_category,
            order_count
        FROM `{self.project_id}.dbt_output.fct_delivery_time_by_zip`
        WHERE avg_delivery_days IS NOT NULL
          AND avg_latitude IS NOT NULL
          AND avg_longitude IS NOT NULL
          AND state IS NOT NULL
          AND order_count >= 5
        ORDER BY avg_delivery_days DESC
        LIMIT 1000
        """
        
        try:
            df = self.client.query(query).to_dataframe()
            print(f"成功加载 {len(df)} 条记录")
            return df
        except Exception as e:
            print(f"从BigQuery获取数据失败: {e}")
            return self.generate_sample_data()
    
    def generate_sample_data(self):
        """生成示例数据（当BigQuery不可用时）"""
        print("生成示例数据...")
        
        import random
        import numpy as np
        
        # 巴西主要城市数据
        cities_data = [
            {'city': 'São Paulo', 'state': 'SP', 'lat': -23.5505, 'lon': -46.6333},
            {'city': 'Rio de Janeiro', 'state': 'RJ', 'lat': -22.9068, 'lon': -43.1729},
            {'city': 'Belo Horizonte', 'state': 'MG', 'lat': -19.9191, 'lon': -43.9386},
            {'city': 'Salvador', 'state': 'BA', 'lat': -12.9714, 'lon': -38.5014},
            {'city': 'Recife', 'state': 'PE', 'lat': -8.0476, 'lon': -34.8770},
            {'city': 'Fortaleza', 'state': 'CE', 'lat': -3.7319, 'lon': -38.5267},
            {'city': 'Brasília', 'state': 'DF', 'lat': -15.8267, 'lon': -47.9218},
            {'city': 'Curitiba', 'state': 'PR', 'lat': -25.4284, 'lon': -49.2733},
            {'city': 'Porto Alegre', 'state': 'RS', 'lat': -30.0346, 'lon': -51.2177},
            {'city': 'Manaus', 'state': 'AM', 'lat': -3.1190, 'lon': -60.0217},
            {'city': 'Belém', 'state': 'PA', 'lat': -1.4558, 'lon': -48.5044},
            {'city': 'Goiânia', 'state': 'GO', 'lat': -16.6869, 'lon': -49.2648},
            {'city': 'Campinas', 'state': 'SP', 'lat': -22.9099, 'lon': -47.0626},
            {'city': 'São Luís', 'state': 'MA', 'lat': -2.5387, 'lon': -44.2825},
            {'city': 'Maceió', 'state': 'AL', 'lat': -9.6658, 'lon': -35.7353},
            {'city': 'Natal', 'state': 'RN', 'lat': -5.7945, 'lon': -35.2110},
            {'city': 'João Pessoa', 'state': 'PB', 'lat': -7.1195, 'lon': -34.8450},
            {'city': 'Aracaju', 'state': 'SE', 'lat': -10.9472, 'lon': -37.0731},
            {'city': 'Teresina', 'state': 'PI', 'lat': -5.0892, 'lon': -42.8019},
            {'city': 'Campo Grande', 'state': 'MS', 'lat': -20.4697, 'lon': -54.6201}
        ]
        
        data = []
        for i, city_info in enumerate(cities_data):
            # 为每个城市生成多个邮编区域
            for j in range(random.randint(3, 8)):
                zip_prefix = f"{(i+1)*10000 + j*1000:05d}"
                
                # 在城市周围生成随机坐标
                lat_offset = random.uniform(-0.5, 0.5)
                lon_offset = random.uniform(-0.5, 0.5)
                
                # 生成送货天数（偏远地区送货时间更长）
                base_days = random.uniform(5, 25)
                if city_info['state'] in ['AM', 'PA', 'AC', 'RO', 'RR', 'AP']:  # 北部州
                    base_days += random.uniform(5, 15)
                elif city_info['state'] in ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']:  # 东北部州
                    base_days += random.uniform(2, 8)
                
                # 分类送货时间
                if base_days <= 10:
                    category = '快速'
                elif base_days <= 15:
                    category = '中等'
                elif base_days <= 20:
                    category = '慢速'
                else:
                    category = '很慢'
                
                data.append({
                    'zip_code_prefix': zip_prefix,
                    'avg_latitude': city_info['lat'] + lat_offset,
                    'avg_longitude': city_info['lon'] + lon_offset,
                    'city': city_info['city'],
                    'state': city_info['state'],
                    'avg_delivery_days': round(base_days, 1),
                    'delivery_category': category,
                    'order_count': random.randint(10, 200)
                })
        
        return pd.DataFrame(data)
    
    def process_data(self, df):
        """处理数据并生成统计信息"""
        # 确保数据类型正确
        df['avg_delivery_days'] = pd.to_numeric(df['avg_delivery_days'], errors='coerce')
        df['order_count'] = pd.to_numeric(df['order_count'], errors='coerce')
        
        # 移除无效数据
        df = df.dropna(subset=['avg_delivery_days', 'avg_latitude', 'avg_longitude'])
        
        # 生成摘要统计
        stats = {
            'total_regions': len(df),
            'total_cities': len(df['city'].unique()),
            'total_states': len(df['state'].unique()),
            'avg_delivery_days': round(df['avg_delivery_days'].mean(), 1),
            'min_delivery_days': round(df['avg_delivery_days'].min(), 1),
            'max_delivery_days': round(df['avg_delivery_days'].max(), 1),
            'total_orders': int(df['order_count'].sum()),
            'last_updated': datetime.datetime.now().isoformat()
        }
        
        return df, stats
    
    def generate_dashboard_data(self, output_file='dashboard_data.json'):
        """生成仪表盘数据文件"""
        # 获取数据
        df = self.fetch_delivery_data()
        
        # 处理数据
        df, stats = self.process_data(df)
        
        # 转换为JSON格式
        data_dict = {
            'stats': stats,
            'data': df.to_dict('records'),
            'states': sorted(df['state'].unique().tolist()),
            'categories': sorted(df['delivery_category'].unique().tolist())
        }
        
        # 保存到文件
        output_path = os.path.join(os.path.dirname(__file__), output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=2)
        
        print(f"数据已保存到: {output_path}")
        print(f"总记录数: {len(df)}")
        print(f"覆盖州数: {stats['total_states']}")
        print(f"平均送货天数: {stats['avg_delivery_days']}")
        
        return output_path

def main():
    """主函数"""
    generator = DeliveryDashboardDataGenerator()
    generator.generate_dashboard_data()

if __name__ == "__main__":
    main()