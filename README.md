1.  요구사항  커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출해 나가 는 과정을 진행합니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다.

   - A. 제공되는 영화 데이터의 주요내용 수집  샘플 영화데이터가 주어집니다. 이중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완 성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

   -  i. 데이터  

     - 1. 제공되는 movie.json 파일을 활용합니다. 

       2. movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.

   -  ii. 결과 

     - 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다. 
     - 가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.

```
def movie_info(movie):
	#딕셔너리 받을 빈통
    movie_info_dict = {}
    #필요한 키값 list에 담기
    key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview','genre_ids']
	#키리스트 요소에 해당하는 값 추출
    for key in key_list:
        movie_info_dict[key] = movie[key]
    #빈통에 넣어줌
    return movie_info_dict
```

```
{'genre_ids': [18, 80],
 'id': 278,
 'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 '
             '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 '
             '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 '
             '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 '
             '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...',
 'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
 'title': '쇼생크 탈출',
 'vote_average': 8.7}
```





2. B제공되는 영화 데이터의 주요내용 수정  (이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완 성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다. )

   ```
   def movie_info(movie, genres):
   	#data file movie.json에 "genre_ids" : [18, 80]으로 저장되어있음
   	#genres.json에서  id값으로 18,80을 가진 값을 찾고 이름을 저장해야 함 ("Drama","Crime")
       genre_ids = movie['genre_ids']
       genre_names = []
       
       #genres파일안에서 id값이 genre_ids랑 같은 애를 찾으면 
       #genre_names에 해당 값이 가진 'name' 추가
       for genre in genres:
           if genre['id'] in genre_ids:
               genre_names.append(genre['name'])
               
   	#딕셔너리 값 gerne_names 제외하고 선언
       key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
   	
   	#새로운 딕셔너리를 담을 깡통 생성
       movie_info_dict = {}
       #ket_list를 돌면서 key값 저장
       #'gerne_names' 깡통에 추가
       for key in key_list:
           movie_info_dict[key] = movie[key]
           movie_info_dict['gerne_names'] = genre_names
       return movie_info_dict
   ```

   

   3.

   ```
   def movie_info(movies, genres):
   
       # 모든 영화 정보 딕셔너리들을 담을 리스트
       movies_info_dict = []
       for movie in movies:
           # 1. movies.json에서 id값 추출하여 변수에 할당
           genre_ids = movie['genre_ids']
   
           # 2. 장르 아이디를 장르 이름으로 변환한 값을 담을 빈통
           gerne_names = []
   
           # 3. genres.json순회
           for genre in genres: 
               # 4. 만약 movie_info의 genre_ids와 일치하는 장르의 아이디가 있을 경우
               if genre['id'] in genre_ids: 
                   # 4-1. gerne_names에 해당 genre['id']의 gerne['name']을 추가한다.
                   gerne_names.append(genre['name']) 
   
   
           ## > 딕셔너리 값 재가공하기 
           # 5. dictionary에 넣을 key에 해당되는 요소를 list에 담기 (gerne_names 제외)
           key_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
   
           # 6. 새로운 dictionary를 담을 변수 선언
           movie_info_dict = {}
   
           # 7. key_list 요소에 해당하는 정보만 추출 (for문 이용)
           for key in key_list:
               movie_info_dict[key] = movie[key]
   
           # 8. 장르 이름 추가
           movie_info_dict['gerne_names'] = gerne_names
   
           # 9. 재가공된 dictionary를 movies_info_dict에 추가
           movies_info_dict.append(movie_info_dict)
   
       # 10. 최종적으로 영화정보들이 담긴 리스트를 반환.
       return movies_info_dict
   ```

   

