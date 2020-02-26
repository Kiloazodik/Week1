{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "listData = pd.read_csv(\"listings.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            id                                               name    host_id  \\\n",
      "0        49091                  COZICOMFORT LONG TERM STAY ROOM 2     266763   \n",
      "1        50646                    Pleasant Room along Bukit Timah     227796   \n",
      "2        56334                                        COZICOMFORT     266763   \n",
      "3        71609                Ensuite Room (Room 1 & 2) near EXPO     367042   \n",
      "4        71896                    B&B  Room 1 near Airport & EXPO     367042   \n",
      "...        ...                                                ...        ...   \n",
      "7902  38105126  Loft 2 pax near Haw Par / Pasir Panjang. Free ...  278109833   \n",
      "7903  38108273                         3bedroom luxury at Orchard  238891646   \n",
      "7904  38109336    [ Farrer Park ] New City Fringe CBD Mins to MRT  281448565   \n",
      "7905  38110493          Cheap Master Room in Central of Singapore  243835202   \n",
      "7906  38112762  Amazing room with private bathroom walk to Orc...   28788520   \n",
      "\n",
      "      host_name neighbourhood_group neighbourhood  latitude  longitude  \\\n",
      "0     Francesca        North Region     Woodlands   1.44255  103.79580   \n",
      "1       Sujatha      Central Region   Bukit Timah   1.33235  103.78521   \n",
      "2     Francesca        North Region     Woodlands   1.44246  103.79667   \n",
      "3       Belinda         East Region      Tampines   1.34541  103.95712   \n",
      "4       Belinda         East Region      Tampines   1.34567  103.95963   \n",
      "...         ...                 ...           ...       ...        ...   \n",
      "7902      Belle      Central Region    Queenstown   1.27973  103.78751   \n",
      "7903       Neha      Central Region       Tanglin   1.29269  103.82623   \n",
      "7904      Mindy      Central Region       Kallang   1.31286  103.85996   \n",
      "7905      Huang      Central Region  River Valley   1.29543  103.83801   \n",
      "7906    Terence      Central Region  River Valley   1.29672  103.83325   \n",
      "\n",
      "            room_type  price  minimum_nights  number_of_reviews last_review  \\\n",
      "0        Private room     83             180                  1  2013-10-21   \n",
      "1        Private room     81              90                 18  2014-12-26   \n",
      "2        Private room     69               6                 20  2015-10-01   \n",
      "3        Private room    206               1                 14  2019-08-11   \n",
      "4        Private room     94               1                 22  2019-07-28   \n",
      "...               ...    ...             ...                ...         ...   \n",
      "7902  Entire home/apt    100               3                  0         NaN   \n",
      "7903  Entire home/apt    550               6                  0         NaN   \n",
      "7904     Private room     58              30                  0         NaN   \n",
      "7905     Private room     56              14                  0         NaN   \n",
      "7906     Private room     65              90                  0         NaN   \n",
      "\n",
      "      reviews_per_month  calculated_host_listings_count  availability_365  \n",
      "0                  0.01                               2               365  \n",
      "1                  0.28                               1               365  \n",
      "2                  0.20                               2               365  \n",
      "3                  0.15                               9               353  \n",
      "4                  0.22                               9               355  \n",
      "...                 ...                             ...               ...  \n",
      "7902                NaN                              31                61  \n",
      "7903                NaN                              34               365  \n",
      "7904                NaN                               3               173  \n",
      "7905                NaN                               2                30  \n",
      "7906                NaN                               7               365  \n",
      "\n",
      "[7907 rows x 16 columns]\n"
     ]
    }
   ],
   "source": [
    "print(listData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id                                   38112762\n",
      "host_id                             288567551\n",
      "host_name                                  ｼﾝ\n",
      "neighbourhood_group               West Region\n",
      "neighbourhood                          Yishun\n",
      "latitude                              1.45459\n",
      "longitude                             103.973\n",
      "room_type                         Shared room\n",
      "price                                   10000\n",
      "minimum_nights                           1000\n",
      "number_of_reviews                         323\n",
      "reviews_per_month                          13\n",
      "calculated_host_listings_count            274\n",
      "availability_365                          365\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "maxValue = listData.max()\n",
    "print(maxValue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id                                   38112762\n",
      "host_id                             288567551\n",
      "host_name                                  ｼﾝ\n",
      "neighbourhood_group               West Region\n",
      "neighbourhood                          Yishun\n",
      "latitude                              1.45459\n",
      "longitude                             103.973\n",
      "room_type                         Shared room\n",
      "price                                   10000\n",
      "minimum_nights                           1000\n",
      "number_of_reviews                         323\n",
      "reviews_per_month                          13\n",
      "calculated_host_listings_count            274\n",
      "availability_365                          365\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "minValue = listData.max()\n",
    "print(minValue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            id                                               name    host_id  \\\n",
      "0        49091                  COZICOMFORT LONG TERM STAY ROOM 2     266763   \n",
      "1        50646                    Pleasant Room along Bukit Timah     227796   \n",
      "2        56334                                        COZICOMFORT     266763   \n",
      "3        71609                Ensuite Room (Room 1 & 2) near EXPO     367042   \n",
      "4        71896                    B&B  Room 1 near Airport & EXPO     367042   \n",
      "...        ...                                                ...        ...   \n",
      "7715  37621650  Comfortable and spacious four-bedroom family s...   43591543   \n",
      "7728  37690516           cozy Condominium in quite neighbourhoods  165475492   \n",
      "7752  37798739                      near Clementi MRT female only  157856583   \n",
      "7766  37841266      Sunny Modern Condo in City Center walk to MRT   39207304   \n",
      "7767  37852422  Private Room With King Size Bed Near Seng Kang...  119880789   \n",
      "\n",
      "      host_name neighbourhood_group neighbourhood  latitude  longitude  \\\n",
      "0     Francesca        North Region     Woodlands   1.44255  103.79580   \n",
      "1       Sujatha      Central Region   Bukit Timah   1.33235  103.78521   \n",
      "2     Francesca        North Region     Woodlands   1.44246  103.79667   \n",
      "3       Belinda         East Region      Tampines   1.34541  103.95712   \n",
      "4       Belinda         East Region      Tampines   1.34567  103.95963   \n",
      "...         ...                 ...           ...       ...        ...   \n",
      "7715     Donald      Central Region       Geylang   1.31410  103.90317   \n",
      "7728  BOONChean      Central Region     Toa Payoh   1.34063  103.88219   \n",
      "7752     Elyssa         West Region      Clementi   1.30677  103.76224   \n",
      "7766     Sophie      Central Region        Rochor   1.30074  103.84742   \n",
      "7767  Christine   North-East Region      Sengkang   1.39324  103.89002   \n",
      "\n",
      "            room_type  price  minimum_nights  number_of_reviews last_review  \\\n",
      "0        Private room     83             180                  1  2013-10-21   \n",
      "1        Private room     81              90                 18  2014-12-26   \n",
      "2        Private room     69               6                 20  2015-10-01   \n",
      "3        Private room    206               1                 14  2019-08-11   \n",
      "4        Private room     94               1                 22  2019-07-28   \n",
      "...               ...    ...             ...                ...         ...   \n",
      "7715  Entire home/apt    699               3                  6  2019-08-23   \n",
      "7728     Private room     60               1                  1  2019-08-12   \n",
      "7752     Private room     56               1                  1  2019-08-17   \n",
      "7766  Entire home/apt    237               7                  1  2019-08-25   \n",
      "7767     Private room     60               1                  1  2019-08-25   \n",
      "\n",
      "      reviews_per_month  calculated_host_listings_count  availability_365  \n",
      "0                  0.01                               2               365  \n",
      "1                  0.28                               1               365  \n",
      "2                  0.20                               2               365  \n",
      "3                  0.15                               9               353  \n",
      "4                  0.22                               9               355  \n",
      "...                 ...                             ...               ...  \n",
      "7715               6.00                              15               189  \n",
      "7728               1.00                               1                 1  \n",
      "7752               1.00                               1               120  \n",
      "7766               1.00                              12               159  \n",
      "7767               1.00                               1               298  \n",
      "\n",
      "[5148 rows x 16 columns]\n"
     ]
    }
   ],
   "source": [
    "newListDataDrop = listData.dropna()\n",
    "print(newListDataDrop)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            id                                               name    host_id  \\\n",
      "0        49091                  COZICOMFORT LONG TERM STAY ROOM 2     266763   \n",
      "1        50646                    Pleasant Room along Bukit Timah     227796   \n",
      "2        56334                                        COZICOMFORT     266763   \n",
      "3        71609                Ensuite Room (Room 1 & 2) near EXPO     367042   \n",
      "4        71896                    B&B  Room 1 near Airport & EXPO     367042   \n",
      "...        ...                                                ...        ...   \n",
      "7902  38105126  Loft 2 pax near Haw Par / Pasir Panjang. Free ...  278109833   \n",
      "7903  38108273                         3bedroom luxury at Orchard  238891646   \n",
      "7904  38109336    [ Farrer Park ] New City Fringe CBD Mins to MRT  281448565   \n",
      "7905  38110493          Cheap Master Room in Central of Singapore  243835202   \n",
      "7906  38112762  Amazing room with private bathroom walk to Orc...   28788520   \n",
      "\n",
      "      host_name neighbourhood_group neighbourhood  latitude  longitude  \\\n",
      "0     Francesca        North Region     Woodlands   1.44255  103.79580   \n",
      "1       Sujatha      Central Region   Bukit Timah   1.33235  103.78521   \n",
      "2     Francesca        North Region     Woodlands   1.44246  103.79667   \n",
      "3       Belinda         East Region      Tampines   1.34541  103.95712   \n",
      "4       Belinda         East Region      Tampines   1.34567  103.95963   \n",
      "...         ...                 ...           ...       ...        ...   \n",
      "7902      Belle      Central Region    Queenstown   1.27973  103.78751   \n",
      "7903       Neha      Central Region       Tanglin   1.29269  103.82623   \n",
      "7904      Mindy      Central Region       Kallang   1.31286  103.85996   \n",
      "7905      Huang      Central Region  River Valley   1.29543  103.83801   \n",
      "7906    Terence      Central Region  River Valley   1.29672  103.83325   \n",
      "\n",
      "            room_type  price  minimum_nights  number_of_reviews last_review  \\\n",
      "0        Private room     83             180                  1  2013-10-21   \n",
      "1        Private room     81              90                 18  2014-12-26   \n",
      "2        Private room     69               6                 20  2015-10-01   \n",
      "3        Private room    206               1                 14  2019-08-11   \n",
      "4        Private room     94               1                 22  2019-07-28   \n",
      "...               ...    ...             ...                ...         ...   \n",
      "7902  Entire home/apt    100               3                  0    NullData   \n",
      "7903  Entire home/apt    550               6                  0    NullData   \n",
      "7904     Private room     58              30                  0    NullData   \n",
      "7905     Private room     56              14                  0    NullData   \n",
      "7906     Private room     65              90                  0    NullData   \n",
      "\n",
      "     reviews_per_month  calculated_host_listings_count  availability_365  \n",
      "0                 0.01                               2               365  \n",
      "1                 0.28                               1               365  \n",
      "2                  0.2                               2               365  \n",
      "3                 0.15                               9               353  \n",
      "4                 0.22                               9               355  \n",
      "...                ...                             ...               ...  \n",
      "7902          NullData                              31                61  \n",
      "7903          NullData                              34               365  \n",
      "7904          NullData                               3               173  \n",
      "7905          NullData                               2                30  \n",
      "7906          NullData                               7               365  \n",
      "\n",
      "[7907 rows x 16 columns]\n"
     ]
    }
   ],
   "source": [
    "newListDataFill = listData.fillna('NullData')\n",
    "print(newListDataFill)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
