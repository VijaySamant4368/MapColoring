indVal = {
    "vertex1": "Ladakh",
    "vertex2": "Jammu and Kashmir",
    "vertex3": "Himachal Pradesh",
    "vertex4": "Andaman and Nicobar Islands",
    "vertex5": "Lakshadweep",
    "vertex6": "Uttarakhand",
    "vertex7": "Haryana",
    "vertex8": "Chandigarh",
    "vertex9": "Punjab",
    "vertex10": "Rajasthan",
    "vertex11": "Delhi",
    "vertex12": "Uttar Pradesh",
    "vertex13": "Dadra and Nagar Haveli",
    "vertex14": "Gujarat",
    "vertex15": "Madhya Pradesh",
    "vertex16": "Bihar",
    "vertex17": "Jharkhand",
    "vertex18": "Maharashtra",
    "vertex19": "Chhattisgarh",
    "vertex20": "Telangana",
    "vertex21": "Karnataka",
    "vertex22": "Andhra Pradesh",
    "vertex23": "Odisha",
    "vertex24": "West Bengal",
    "vertex25": "Sikkim",
    "vertex26": "Arunachal Pradesh",
    "vertex27": "Nagaland",
    "vertex28": "Manipur",
    "vertex29": "Assam",
    "vertex30": "Mizoram",
    "vertex31": "Tripura",
    "vertex32": "Meghalaya",
    "vertex33": "Puducherry",
    "vertex34": "Tamil Nadu",
    "vertex35": "Kerala",
    "vertex36": "Goa"
}

ind=[[0],# Ladakh
[1,0], #J&K
[1,1,0], #HP
[0,0,0,0],# A&N
[0,0,0,0,0], #Lakshadweep
[0,0,1,0,0,0], #Uttarakhand
[0,0,1,0,0,0,0], #Haryana
[0,0,0,0,0,0,1,0], #Chandigarh
[0,1,1,0,0,0,1,1,0], #Punjab
[0,0,0,0,0,0,1,0,1,0], #Rajasthan
[0,0,0,0,0,0,1,0,0,0,0], #Delhi
[0,0,0,0,0,1,1,0,0,1,1,0], #UP
[0,0,0,0,0,0,0,0,0,0,0,0,0], #Dadra and Nagar Haveli
[0,0,0,0,0,0,0,0,0,1,0,0,1,0], #Gujarat
[0,0,0,0,0,0,0,0,0,1,0,1,0,1,0], #MP
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0], #Bihar
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0], #Jharkhand
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0], #Maharashtra
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0], #Chhatisgarh
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],	#20,Telangana

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0], #Karnataka
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0], #Andhra Pradesh
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0], #Odisha 
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0], #Bengal
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],	#25 Sikkim

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Arunachal
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], #Nagaland
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], #Manipur
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0],# Assam
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],#30 Mizoram

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0], #Tripura
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],# Meghalaya
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0], #Puducherry
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0], #Tamil Nadu
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0], #Kerala
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]# Goa




punjabValues={
    "vertex1": "Pathankot",
    "vertex2": "Gurdaspur",
    "vertex3": "Amritsar",
    "vertex4": "Hoshiarpur",
    "vertex5": "Tarn Taran",
    "vertex6": "Kapurthala",
    "vertex7": "Ferozpur",
    "vertex8": "Jalandhar",
    "vertex9": "Nawanshahr",
    "vertex10": "Rupnagar",
    "vertex11": "Fazilka",
    "vertex12": "Faridkot",
    "vertex13": "Moga",
    "vertex14": "Ludhiana",
    "vertex15": "S.A.S. Nagar",
    "vertex16": "Muktsar",
    "vertex17": "Barnala",
    "vertex18": "Malerkotla",
    "vertex19": "Fatehgarh Sahib",
    "vertex20": "Bathinda",
    "vertex21": "Mansa",
    "vertex22": "Sangrur",
    "vertex23": "Patiala"
    }

punjab=[[0], 
      [1, 0], 
      [0, 1, 0], 
      [0, 1, 0, 0], 
      [0, 0, 1, 0, 0], 
      [0, 1, 1, 1, 1, 0], 
      [0, 0, 0, 0, 1, 1, 0], 
      [0, 0, 0, 1, 0, 1, 1, 0], 
      [0, 0, 0, 1, 0, 1, 0, 1, 0], 
      [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0]]

g1=[[0],[1,0],[0,1,0],[0,1,1,0],[0,0,0,1,0],[1,0,0,0,1,0],[1,0,1,0,1,1]]
v1={
    "vertex1": "a",
    "vertex2": "b",
    "vertex3": "c",
    "vertex4": "d",
    "vertex5": "e",
    "vertex6": "f",
    "vertex7": "g"}

