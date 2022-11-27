## Phonetic Transcrition

The phonetic transcription below is based on the scheme found in *Arabic Through the Quran* by Alan Jones (Islamic Texts Society, 2008). The correct form of pronunciation will depend on context, especially for the letters *hamza* and *alif maksūra*. The basic form of transcription is shown below.



### Phonetic transcription for letters

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Letter</th>
      <th>Transcription</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>alif</td>
      <td>ā</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bā</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tā</td>
      <td>t</td>
    </tr>
    <tr>
      <th>3</th>
      <td>thā</td>
      <td>th</td>
    </tr>
    <tr>
      <th>4</th>
      <td>jīm</td>
      <td>j</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ḥā</td>
      <td>ḥ</td>
    </tr>
    <tr>
      <th>6</th>
      <td>khā</td>
      <td>kh</td>
    </tr>
    <tr>
      <th>7</th>
      <td>dāl</td>
      <td>d</td>
    </tr>
    <tr>
      <th>8</th>
      <td>dhāl</td>
      <td>dh</td>
    </tr>
    <tr>
      <th>9</th>
      <td>rā</td>
      <td>r</td>
    </tr>
    <tr>
      <th>10</th>
      <td>zāy</td>
      <td>z</td>
    </tr>
    <tr>
      <th>11</th>
      <td>sīn</td>
      <td>s</td>
    </tr>
    <tr>
      <th>12</th>
      <td>shīn</td>
      <td>sh</td>
    </tr>
    <tr>
      <th>13</th>
      <td>ṣād</td>
      <td>ṣ</td>
    </tr>
    <tr>
      <th>14</th>
      <td>ḍād</td>
      <td>ḍ</td>
    </tr>
    <tr>
      <th>15</th>
      <td>ṭā</td>
      <td>ṭ</td>
    </tr>
    <tr>
      <th>16</th>
      <td>ẓā</td>
      <td>ẓ</td>
    </tr>
    <tr>
      <th>17</th>
      <td>ʿayn</td>
      <td>ʿ</td>
    </tr>
    <tr>
      <th>18</th>
      <td>ghayn</td>
      <td>gh</td>
    </tr>
    <tr>
      <th>19</th>
      <td>fā</td>
      <td>f</td>
    </tr>
    <tr>
      <th>20</th>
      <td>qāf</td>
      <td>q</td>
    </tr>
    <tr>
      <th>21</th>
      <td>kāf</td>
      <td>k</td>
    </tr>
    <tr>
      <th>22</th>
      <td>lām</td>
      <td>l</td>
    </tr>
    <tr>
      <th>23</th>
      <td>mīm</td>
      <td>m</td>
    </tr>
    <tr>
      <th>24</th>
      <td>nūn</td>
      <td>n</td>
    </tr>
    <tr>
      <th>25</th>
      <td>hā</td>
      <td>h</td>
    </tr>
    <tr>
      <th>26</th>
      <td>wāw</td>
      <td>w</td>
    </tr>
    <tr>
      <th>27</th>
      <td>yā</td>
      <td>y</td>
    </tr>
    <tr>
      <th>28</th>
      <td>hamza</td>
      <td>'</td>
    </tr>
    <tr>
      <th>29</th>
      <td>alif maksura</td>
      <td>ā</td>
    </tr>
    <tr>
      <th>30</th>
      <td>ta marbūta</td>
      <td>t</td>
    </tr>
  </tbody>
</table>

### Phonetic transcription for diactrics

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Diacritic</th>
      <th>Transcription</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>fathatan</td>
      <td>an</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dammatan</td>
      <td>un</td>
    </tr>
    <tr>
      <th>2</th>
      <td>kasratan</td>
      <td>in</td>
    </tr>
    <tr>
      <th>3</th>
      <td>fatha</td>
      <td>a</td>
    </tr>
    <tr>
      <th>4</th>
      <td>damma</td>
      <td>u</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kasra</td>
      <td>i</td>
    </tr>
    <tr>
      <th>6</th>
      <td>shadda</td>
      <td>(double)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>sukūn</td>
      <td>'</td>
    </tr>
  </tbody>
</table>

The long vowels are indicated by *ā*, *ī* and *ū*, and the *maddah* may also be used to lengthen a vowel. The *shadda* is indicated by the doubling of a letter



## Usage

- **Python 3.9 required**

```bash
python phonetic.py [-t arab_text] [-f arab_file]
```

**Ex**.

```bash
python phonetic.py "إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَٱلَّذِينَ هَادُوا۟ وَٱلنَّصَـٰرَىٰ وَٱلصَّـٰبِـِٔينَ مَنْ ءَامَنَ بِٱللَّهِ وَٱلْيَوْمِ ٱلْـَٔاخِرِ وَعَمِلَ صَـٰلِحًۭا فَلَهُمْ أَجْرُهُمْ عِندَ رَبِّهِمْ وَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُ
```

**output**

```
'inna l-adhīna 'āmanū wālladhīna hādū wālnnaṣaāraā wālṣṣaābiīna man 'āmana bil-lahi wālyawmi l-ākhiri waʿamila ṣal-iḥan falahum 'ajruhum ʿinda rabbihim walā khawfun ʿalayhim walā hum yaḥzanūna
```



## Contributors

Feel free to contribute by making pull-requests or writing issues. Thanks
