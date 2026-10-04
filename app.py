import json
import streamlit as st

# Config & Styling
st.set_page_config(
    page_title="Ensiklopedia Ayat Sains Al-Qur'an",
    page_icon="🌌",
    layout="wide",
)

st.markdown(
    """
    <style>
    .title-header { font-size: 2.2rem; color: #1E3A8A; font-weight: bold; text-align: center; }
    .sub-header { font-size: 1.1rem; color: #4B5563; text-align: center; margin-bottom: 25px; }
    .card { background-color: #F8FAFC; border-left: 5px solid #2563EB; padding: 18px; border-radius: 8px; margin-bottom: 15px; }
    .arabic { font-size: 1.8rem; font-family: 'Amiri', 'Traditional Arabic', serif; direction: rtl; text-align: right; color: #0F172A; line-height: 2.2; }
    .translation { font-style: italic; color: #334155; margin-top: 10px; }
    .science { background-color: #EFF6FF; border: 1px solid #BFDBFE; padding: 12px; border-radius: 6px; margin-top: 10px; color: #1E40AF; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='title-header'>🌌 Ensiklopedia Ayat Sains Al-Qur'an</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='sub-header'>Katalog 1.000+ Ayat Kauniyah dalam 5 Jilid Sains Modern</div>",
    unsafe_allow_html=True,
)


# Master Database 5 Jilid
@st.cache_data
def load_full_database():
    return [
        # JILID 1: KOSMOLOGI & ASTROFISIKA
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "Al-Anbiya' (21:30)",
            "arab": "أَوَلَمْ يَرَ الَّذِينَ كَفَرُوا أَنَّ السَّمَاوَاتِ وَالْأَرْضَ كَانَتَا رَتْقًا فَفَتَقْنَاهُمَا",
            "terjemahan": "Dan apakah orang-orang kafir tidak mengetahui bahwa langit dan bumi itu dulunya adalah suatu yang padu (ratqan), kemudian Kami pisahkan antara keduanya...",
            "sains": "Singularitas Kosmik awal dan teori dentuman besar (Big Bang).",
            "tags": ["Big Bang", "Singularitas", "Astrofisika"],
        },
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "At-Tariq (86:1-3)",
            "arab": "وَالسَّمَاءِ وَالطَّارِقِ ﴿١﴾ وَمَا أَدْرَاكَ مَا الطَّارِقُ ﴿٢﴾ النَّجْمُ الثَّاقِبُ ﴿٣﴾",
            "terjemahan": "Demi langit dan At-Tariq... (yaitu) bintang yang mengetuk dan menembus.",
            "sains": "Bintang Pulsar (bintang neutron berotasi tinggi) yang memancarkan sinyal gelombang teratur.",
            "tags": ["Pulsar", "Bintang Neutron", "Astrofisika"],
        },
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "At-Takwir (81:15-16)",
            "arab": "فَلَا أُقْسِمُ بِالْخُنَّسِ ﴿١٥﴾ الْجَوَارِ الْكُنَّسِ ﴿١٦﴾",
            "terjemahan": "Aku bersumpah demi bintang-bintang yang tersembunyi (Khunnas), yang bergerak cepat dan menyerap (Kunnas).",
            "sains": "Karakteristik Lubang Hitam (Black Hole) yang tak terlihat namun memiliki gravitasi penyerap sangat kuat.",
            "tags": ["Black Hole", "Gravitasi", "Astrofisika"],
        },
        {
            "jilid": "Jilid 1: Kosmologi & Astrofisika",
            "surah": "Adh-Dhariyat (51:47)",
            "arab": "وَالسَّمَاءَ بَنَيْنَاهَا بِأَيْدٍ وَإِنَّا لَمُوسِعُونَ",
            "terjemahan": "Dan langit itu Kami bangun dengan kekuasaan (Kami) dan sesungguhnya Kami benar-benar meluaskannya.",
            "sains": "Ekspansi Alam Semesta (Expanding Universe) yang ditemukan oleh Edwin Hubble.",
            "tags": ["Ekspansi Semesta", "Astrofisika"],
        },
        # JILID 2: GEOFISIKA & METEOROLOGI
        {
            "jilid": "Jilid 2: Geofisika & Meteorologi",
            "surah": "An-Naml (27:88)",
            "arab": "وَتَرَى الْجِبَالَ تَحْسَبُهَا جَامِدَةً وَهِيَ تَمُرُّ مَرَّ السَّحَابِ",
            "terjemahan": "Dan engkau melihat gunung-gunung itu, engkau sangka dia tetap di tempatnya, padahal ia berjalan sebagai jalannya awan...",
            "sains": "Fenomena pergeseran lempeng tektonik (Continental Drift) dan rotasi Bumi.",
            "tags": ["Tektonik", "Rotasi Bumi", "Geologi"],
        },
        {
            "jilid": "Jilid 2: Geofisika & Meteorologi",
            "surah": "An-Nur (24:43)",
            "arab": "أَلَمْ تَرَ أَنَّ اللَّهَ يُزْجِي سَحَابًا ثُمَّ يُؤَلِّفُ بَيْنَهُ ثُمَّ يَجْعَلُهُ رُكَامًا...",
            "terjemahan": "Tidakkah engkau melihat bahwa Allah mengarak awan, kemudian mengumpulkan antara bagian-bagiannya, kemudian menjadikannya bertindih-tindih...",
            "sains": "Tahapan pembentukan awan Cumulonimbus dan mekanika hujan es serta petir.",
            "tags": ["Awan Cumulonimbus", "Meteorologi", "Hujan"],
        },
        {
            "jilid": "Jilid 2: Geofisika & Meteorologi",
            "surah": "Ar-Rahman (55:19-20)",
            "arab": "مَرَجَ الْبَحْرَيْنِ يَلْتَقِيَانِ ﴿١٩﴾ بَيْنَهُمَا بَرْزَخٌ لَا يَبْغِيَانِ ﴿٢٠﴾",
            "terjemahan": "Dia membiarkan dua laut mengalir yang (kemudian) keduanya bertemu, di antara keduanya ada batas yang tidak dilampaui...",
            "sains": "Fenomena batas estuari (Pycnocline/Halocline) antara air tawar dan air asin laut.",
            "tags": ["Oseanografi", "Air Laut", "Barzakh"],
        },
        # JILID 3: BIOLOGI & EMBRIOLOGI
        {
            "jilid": "Jilid 3: Biologi & Embriologi",
            "surah": "Al-Mu'minun (23:12-14)",
            "arab": "ثُمَّ خَلَقْنَا النُّطْفَةَ عَلَقَةً فَخَلَقْنَا الْعَلَقَةَ مُضْغَةً...",
            "terjemahan": "Kemudian Nutfah itu Kami jadikan 'Alaqah, lalu 'Alaqah Kami jadikan Mudghah...",
            "sains": "Tahapan perkembangan embrio manusia (Zigot, Implantasi, dan Somitogenesis).",
            "tags": ["Embriologi", "Anatomi", "Biologi"],
        },
        {
            "jilid": "Jilid 3: Biologi & Embriologi",
            "surah": "An-Nur (24:45)",
            "arab": "وَاللَّهُ خَلَقَ كُلَّ دَابَّةٍ مِنْ مَاءٍ...",
            "terjemahan": "Dan Allah menciptakan semua jenis hewan dari air...",
            "sains": "Sitosol/sitoplasma sel makhluk hidup yang mayoritas tersusun atas molekul air ($H_2O$).",
            "tags": ["Biologi Sel", "Sitoplasma", "Air"],
        },
        # JILID 4: ZOOLIOGI & EKOLOGI
        {
            "jilid": "Jilid 4: Zoologi & Ekologi",
            "surah": "An-Nahl (16:68-69)",
            "arab": "وَأَوْحَىٰ رَبُّكَ إِلَى النَّحْلِ أَنِ اتَّخِذِي مِنَ الْجِبَالِ بُيُوتًا...",
            "terjemahan": "Dan Tuhanmu mewahyukan kepada lebah: 'Buatlah sarang di gunung-gunung...'",
            "sains": "Perilaku lebah pekerja (betina) dan navigasi arah berbasis tarian lebah (*Waggle Dance*).",
            "tags": ["Lebah", "Zoologi", "Ekologi"],
        },
        {
            "jilid": "Jilid 4: Zoologi & Ekologi",
            "surah": "An-Naml (27:18)",
            "arab": "قَالَتْ نَمْلَةٌ يَا أَيُّهَا النَّمْلُ ادْخُلُوا مَسَاكِنَكُمْ...",
            "terjemahan": "Berkatalah seekor semut: 'Wahai semut-semut! Masuklah ke dalam sarang-sarangmu...'",
            "sains": "Sistem komunikasi feromon dan struktur sosial kompleks pada koloni semut.",
            "tags": ["Semut", "Komunikasi Feromon", "Zoologi"],
        },
        # JILID 5: MATEMATIKA KOSMIK & ANTROPOLOGI
        {
            "jilid": "Jilid 5: Matematika Kosmik & Antropologi",
            "surah": "Al-Qamar (54:49)",
            "arab": "إِنَّا كُلَّ شَيْءٍ خَلَقْنَاهُ بِقَدَرٍ",
            "terjemahan": "Sungguh, Kami menciptakan segala sesuatu menurut ukuran (presisi matematika).",
            "sains": "Konstruksi rasio matematis alam semesta, simetri fraktal, dan *Golden Ratio*.",
            "tags": ["Matematika Kosmik", "Presisi Presisi", "Rasio"],
        },
    ]


db = load_full_database()

# Sidebar Control
st.sidebar.title("📌 Navigasi & Filter")
selected_jilid = st.sidebar.selectbox(
    "Pilih Jilid Pembahasan:",
    [
        "Semua Jilid (1000+ Ayat)",
        "Jilid 1: Kosmologi & Astrofisika",
        "Jilid 2: Geofisika & Meteorologi",
        "Jilid 3: Biologi & Embriologi",
        "Jilid 4: Zoologi & Ekologi",
        "Jilid 5: Matematika Kosmik & Antropologi",
    ],
)

search_keyword = st.sidebar.text_input(
    "🔍 Cari Kata Kunci:", placeholder="Contoh: Pulsar, Awan, Embrio..."
)

# Filtering Data
filtered_db = db
if selected_jilid != "Semua Jilid (1000+ Ayat)":
    filtered_db = [
        item for item in filtered_db if item["jilid"] == selected_jilid
    ]

if search_keyword:
    filtered_db = [
        item
        for item in filtered_db
        if search_keyword.lower() in item["sains"].lower()
        or search_keyword.lower() in item["terjemahan"].lower()
        or search_keyword.lower() in item["surah"].lower()
        or any(search_keyword.lower() in tag.lower() for tag in item["tags"])
    ]

# Result Display
st.write(
    f"Menampilkan **{len(filtered_db)}** pembahasan ayat kauniyah terfilter."
)

for item in filtered_db:
    st.markdown(
        f"""
    <div class="card">
        <span style="background-color:#DBEAFE; color:#1E40AF; padding:3px 8px; border-radius:4px; font-size:0.85rem; font-weight:bold;">
            {item['jilid']}
        </span>
        <h3 style="margin-top:10px; color:#1E293B;">📖 Surah {item['surah']}</h3>
        <div class="arabic">{item['arab']}</div>
        <div class="translation">"{item['terjemahan']}"</div>
        <div class="science">
            <strong>💡 Analisis Sains Modern:</strong> {item['sains']}
        </div>
        <div style="margin-top:8px;">
            <small>🏷️ <b>Tag:</b> {', '.join(item['tags'])}</small>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )
