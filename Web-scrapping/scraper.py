"""
Модуль для веб-скраппинга статей с Хабра.

Содержит функции:
- get_articles_from_page — получает список статей с preview-информацией.
- filter_articles_by_keywords — фильтрует статьи по ключевым словам.
- get_full_article_text — получает полный текст статьи (для доп. задания).
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional


def get_articles_from_page(url: str) -> List[Dict[str, str]]:
    """
    Получает список статей с указанной страницы Хабра.

    Args:
        url: URL страницы со свежими статьями.

    Returns:
        Список словарей с информацией о статьях:
        [{'date': ..., 'title': ..., 'link': ..., 'preview': ...}, ...]
    """
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36'
        )
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    
    # Ищем все карточки статей
    for card in soup.find_all('article', class_='tm-articles-list__item'):
        try:
            # Дата публикации
            date_tag = card.find('time')
            date = date_tag.get('datetime', '') if date_tag else ''
            
            # Заголовок
            title_tag = card.find('a', class_='tm-title__link')
            if not title_tag:
                continue
            title = title_tag.get_text(strip=True)
            
            # Ссылка
            link = 'https://habr.com' + title_tag.get('href', '')
            
            # Preview-текст (краткое описание)
            preview_tag = card.find('div', class_='tm-article-body')
            preview = preview_tag.get_text(strip=True) if preview_tag else ''
            
            # Если preview пустой, пробуем взять из другого места
            if not preview:
                preview_tag = card.find('div', class_='tm-article-snippet__lead')
                preview = preview_tag.get_text(strip=True) if preview_tag else ''
            
            articles.append({
                'date': date,
                'title': title,
                'link': link,
                'preview': preview,
            })
        except AttributeError:
            continue
    
    return articles


def filter_articles_by_keywords(
    articles: List[Dict[str, str]],
    keywords: List[str],
    search_in_full_text: bool = False,
) -> List[Dict[str, str]]:
    """
    Фильтрует статьи по ключевым словам.

    Args:
        articles: список статей (из get_articles_from_page).
        keywords: список ключевых слов для поиска.
        search_in_full_text: если True — искать в полном тексте статьи,
            иначе только в preview.

    Returns:
        Отфильтрованный список статей.
    """
    filtered = []
    
    for article in articles:
        # Определяем, где искать: в preview или в полном тексте
        if search_in_full_text:
            text_to_search = get_full_article_text(article['link'])
        else:
            text_to_search = article.get('preview', '')
        
        # Приводим к нижнему регистру для регистронезависимого поиска
        text_lower = text_to_search.lower()
        
        # Проверяем, есть ли хотя бы одно ключевое слово
        if any(keyword.lower() in text_lower for keyword in keywords):
            filtered.append(article)
    
    return filtered


def get_full_article_text(article_url: str) -> str:
    """
    Получает полный текст статьи по её URL (для дополнительного задания).

    Args:
        article_url: URL статьи.

    Returns:
        Полный текст статьи.
    """
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/120.0.0.0 Safari/537.36'
        )
    }
    
    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ищем основной текст статьи
        article_body = soup.find('div', class_='article-formatted-body')
        if article_body:
            return article_body.get_text(strip=True)
        
        # Альтернативный вариант для нового дизайна
        article_body = soup.find('div', class_='tm-article-body')
        if article_body:
            return article_body.get_text(strip=True)
        
        return ''
    except requests.RequestException:
        return ''