# project

1. open api를 활용한 DB 가져오기 (Pull)
2. 데이터 저장 (Store)
3. API 서비스 개발
4. 데이터 분석용 대시보드 개발

주제 : House Sales in King County, USA

# column
id	
date 매매일자
price 가격
bedrooms 침실
bathrooms 욕실
sqft_living 거주하는 건물 면적
sqft_lot 대지 면적
floors 층 -	Number of floors
waterfront - 수변 ‘1’ if the property has a waterfront, ‘0’ if not.
view  - An index from 0 to 4 of how good the view of the property was
condition - Condition of the house, ranked from 1 to 5
grade - Classification by construction quality which refers to the types of materials used and the quality of workmanship. Buildings of better quality (higher grade) cost more to build per unit of measure and command higher value. Additional information in: KingCounty
sqft_above 지상층 면적
sqft_basement 지하층의 면적
yr_built - 	Year built
yr_renovated - Year renovated. ‘0’ if never renovated
zipcode - 5 digit zip code
lat - 	Latitude
long - 	Longitude
sqft_living15 - Average size of interior housing living space for the closest 15 houses, in square feet
sqft_lot15 - 	Average size of land lots for the closest 15 houses, in square feet

sqft_living = sqft_above + sqft_basement


