"""
Основной модуль для запуска скрипта веб-скраппинга.

Парсит страницу со свежими статьями Хабра и выводит те,
которые содержат хотя бы одно из ключевых слов.
"""

from scraper import get_articles_from_page, filter_articles_by_keywords


# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def main():
    """Основная функция для запуска скрипта."""
    url = 'https://habr.com/ru/all/'
    
    print(f"Парсим страницу: {url}")
    print(f"Ключевые слова: {', '.join(KEYWORDS)}")
    print("-" * 60)
    
    # Получаем статьи
    articles = get_articles_from_page(url)
    print(f"Найдено статей на странице: {len(articles)}")
    
    # Фильтруем по ключевым словам (по preview-информации)
    filtered = filter_articles_by_keywords(articles, KEYWORDS)
    
    # Выводим результаты
    print(f"\nПодходящих статей: {len(filtered)}")
    print("=" * 60)
    
    for article in filtered:
        print(f"{article['date']} – {article['title']} – {article['link']}")
    


if __name__ == '__main__':
    main()