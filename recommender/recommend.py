from process_data import prepare_data, load_data


def prepare(preferred_genres):
    # try:
    #     tfidf_matrix, cosine_sim, indices, dataframe = load_data()
    # except FileNotFoundError:
    #     print("Preparing data...")
    #     tfidf_matrix, cosine_sim, indices, dataframe = prepare_data('../movie_crawl/output/movie.csv', preferred_genres)

    # print("Preparing data...")
    # tfidf_matrix, cosine_sim, indices, dataframe = prepare_data('../movie_crawl/output/movie.csv', preferred_genres)
    print("Loading data...")
    tfidf_matrix, cosine_sim, indices, dataframe = load_data()
    return cosine_sim, indices, dataframe


def recommend(movie_ids, preferred_genres):
    # print("Loading data...")
    # tfidf_matrix, cosine_sim, indices, dataframe = load_data()
    print("Preparing data...")
    tfidf_matrix, cosine_sim, indices, dataframe = prepare_data('../movie_crawl/output/movie.csv', preferred_genres)
    result = set()
    # print(indices)
    print(dataframe.iloc[:17, [0, 1]])

    for movie_id in movie_ids:
        # idx = indices[movie_id]
        idx = movie_id
        # print(idx, dataframe["title"][idx])

        # Get similarity scores for the selected movie
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]  # Exclude the movie itself from recommendations

        # Get indices of recommended movies
        movie_indices = [i[0] for i in sim_scores]

        # Add recommended movie indices to the set
        result.update(movie_indices)

        # Convert set to list and get the first 10 movies
    result = list(result)[:20]

    print('< 추천 영화 >')
    for i, idx in enumerate(result):
        print(f'{i + 1} : {dataframe["title"][idx]} {idx}')

    return result


# def recommend(title, preferred_genres):
#     cosine_sim, indices, dataframe = prepare(preferred_genres)
#     result = []
#     idx = indices[title]
#
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#
#     sim_scores = sim_scores[1:11]
#
#     movie_indices = [i[0] for i in sim_scores]
#
#     for i in range(10):
#         result.append(dataframe['title'][movie_indices[i]])
#
#     print('< 추천 영화 >')
#     for i in range(10):
#         print(str(i + 1) + ' : ' + result[i])


if __name__ == "__main__":
    # recommend('곤지암')
    # recommend(['조제', '말아톤', '가을로'], ['액션', '범죄'])
    recommend([16, 692, 687], ['액션', '범죄'])
    # recommend_list(['곤지암', '공작', '감기'])
    # recommend_list(['여고괴담 5', '부산행', '기생충'])
