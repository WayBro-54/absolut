INSERT INTO dictionaries_statusdelivery (id, name, code, is_active) VALUES
(1, 'Создана', 'created', true),
(2, 'В пути', 'in_transit', true),
(3, 'Доставлена', 'delivered', true)
on conflict (id) do nothing;

INSERT INTO dictionaries_service (id, name, code, is_active) VALUES
(1, 'Экспресс-доставка', 'express', true),
(2, 'Стандартная доставка', 'standard', true)
on conflict (id) do nothing;

INSERT INTO dictionaries_transport (id, name, code, is_active) VALUES
(1, 'А 100 АА', 'А100АА', true),
(2, 'Б 111 ББ', 'BB111BB', true),
(3, 'В 222 ВВ', 'V222VV', true)
on conflict (id) do nothing;

INSERT INTO dictionaries_typecargo (id, name, code, is_active) VALUES
(1, 'Хрупкий', 'fragile', true),
(2, 'Опасный', 'hazardous', true),
(3, 'Обычный', 'regular', true)
on conflict (id) do nothing;

INSERT INTO dictionaries_typepackaging (id, name, code, is_active) VALUES
(1, 'Коробка', 'box', true),
(2, 'Паллета', 'pallet', true),
(3, 'Конверт', 'envelope', true)
on conflict (id) do nothing;
