import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

day_df = pd.read_csv("dashboard/day_data.csv")
day_df.head()


# Menyiapkan df_penyewaan_harian
def buat_df_penyewaan_harian(df):
    df_penyewaan_harian = df.groupby(by='tanggal').agg({
        'jumlah': 'sum'
    }).reset_index()
    return df_penyewaan_harian

# Menyiapkan df_casual_penyewaan_harian
def buat_df_casual_penyewaan_harian(df):
    df_casual_penyewaan_harian = df.groupby(by='tanggal').agg({
        'casual': 'sum'
    }).reset_index()
    return df_casual_penyewaan_harian

# Menyiapkan df_registered_penyewaan_harian
def buat_df_registered_penyewaan_harian(df):
    df_registered_penyewaan_harian = df.groupby(by='tanggal').agg({
        'registered': 'sum'
    }).reset_index()
    return df_registered_penyewaan_harian
    
# Menyiapkan df_penyewaan_musiman
def buat_df_penyewaan_musiman(df):
    df_penyewaan_musiman = df.groupby(by='musim')[['registered', 'casual']].sum().reset_index()
    return df_penyewaan_musiman

# Menyiapkan df_penyewaan_bulanan
def buat_df_penyewaan_bulanan(df):
    df_penyewaan_bulanan = df.groupby(by='bulan').agg({
        'jumlah': 'sum'
    })
    ordered_bulans = [
        'Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
        'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'
    ]
    df_penyewaan_bulanan = df_penyewaan_bulanan.reindex(ordered_bulans, fill_value=0)
    return df_penyewaan_bulanan

# Menyiapkan hari_rent_df
def create_hari_rent_df(df):
    hari_rent_df = df.groupby(by='hari').agg({
        'jumlah': 'sum'
    }).reset_index()
    return hari_rent_df

# Menyiapkan df_penyewaan_tergantung_kondisi_cuaca
def buat_df_penyewaan_tergantung_kondisi_cuaca(df):
    df_penyewaan_tergantung_kondisi_cuaca = df.groupby(by='kondisi_cuaca').agg({
        'jumlah': 'sum'
    })
    return df_penyewaan_tergantung_kondisi_cuaca


# Membuat komponen filter
min_date = pd.to_datetime(day_df['tanggal']).dt.date.min()
max_date = pd.to_datetime(day_df['tanggal']).dt.date.max()
 
with st.sidebar:
    st.image('https://st2.depositphotos.com/40527348/44435/v/450/depositphotos_444356130-stock-illustration-bicycle-rental-icons-set-logo.jpg')
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['tanggal'] >= str(start_date)) & 
                (day_df['tanggal'] <= str(end_date))]

# Menyiapkan berbagai dataframe
df_penyewaan_harian = buat_df_penyewaan_harian(main_df)
df_casual_penyewaan_harian = buat_df_casual_penyewaan_harian(main_df)
df_registered_penyewaan_harian = buat_df_registered_penyewaan_harian(main_df)
df_penyewaan_musiman = buat_df_penyewaan_musiman(main_df)
df_penyewaan_bulanan = buat_df_penyewaan_bulanan(main_df)
hari_rent_df = create_hari_rent_df(main_df)
df_penyewaan_tergantung_kondisi_cuaca = buat_df_penyewaan_tergantung_kondisi_cuaca(main_df)


# Membuat Dashboard secara lengkap

# Membuat judul
st.header('Dashboard penyewaan sepeda 🚲')

# Membuat jumlah penyewaan harian
st.subheader('Sewa Harian')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = df_casual_penyewaan_harian['casual'].sum()
    st.metric('Pengguna Biasa', value= daily_rent_casual)

with col2:
    daily_rent_registered = df_registered_penyewaan_harian['registered'].sum()
    st.metric('Pengguna Terdaftar', value= daily_rent_registered)
 
with col3:
    daily_rent_total = df_penyewaan_harian['jumlah'].sum()
    st.metric('Total Pengguna', value= daily_rent_total)

# Membuat jumlah penyewaan berdasarkan musim
st.subheader('Jumlah Penyewaan Musiman')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='musim',
    y='registered',
    data=df_penyewaan_musiman,
    label='Registered',
    color='tab:blue',
    ax=ax
)

sns.barplot(
    x='musim',
    y='casual',
    data=df_penyewaan_musiman,
    label='Casual',
    color='tab:orange',
    ax=ax
)

for index, row in df_penyewaan_musiman.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

# Membuat korelasi antara suhu, kecepatan angin, dan kelembaban dengan jumlah penyewa
st.subheader('Korelasi suhu, kecepatan angin, kelembaban dengan jumlah penyewa')

fig, ax = plt.subplots(figsize=(16, 8))

plt.subplot(1, 3, 1)
sns.regplot(
    x='suhu',
    y='jumlah',
    data=day_df,
)
plt.title('Korelasi suhu dengan jumlah penyewa')

plt.subplot(1, 3, 2)
sns.regplot(
    x='kecepatan_angin',
    y='jumlah',
    data=day_df,
)
plt.title('Korelasi kecepatan angin dengan jumlah penyewa')

plt.subplot(1, 3, 3)
sns.regplot(
    x='kelembaban',
    y='jumlah',
    data=day_df,
)
plt.title('Korelasi kelembaban dengan jumlah penyewa')

# Menampilkan visualisasi di dashboard
st.pyplot(fig)

# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Penyewaan tergantung kondisi cuaca')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=df_penyewaan_tergantung_kondisi_cuaca.index,
    y=df_penyewaan_tergantung_kondisi_cuaca['jumlah'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(df_penyewaan_tergantung_kondisi_cuaca['jumlah']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

st.caption('Copyright (c) Muhammad Aqil Alhafizh 2024')
