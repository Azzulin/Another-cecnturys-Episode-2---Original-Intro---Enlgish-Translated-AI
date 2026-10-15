"""UI translations for build 0.0.2, keyed by the Japanese source (never by position) and written as _fill files.
Proper names marked TENTATIVE wait for the glossary research (work/glossary/research/)."""
import json

EN = r"D:\Ace 2\work\translation\en\%s.json"
FILL = r"D:\Ace 2\work\translation\en\_fill\%s.json"

HUD3020 = {
 'アビリティ１': 'Ability 1', 'アビリティ２': 'Ability 2', 'アビリティ３': 'Ability 3', '近接': 'Melee',
 **{'ウェポン' + '１２３４５６７'[i]: 'Weapon %d' % (i + 1) for i in range(7)},
 **{'コンボ' + n: 'Combo %d' % (i + 1) for i, n in enumerate(['１', '２', '３', '４', '５', '６', '７', '８', '９', '１０'])},
 'サブコンボ１': 'Sub Combo 1', 'サブコンボ２': 'Sub Combo 2', 'サブコンボ３': 'Sub Combo 3', 'サブコンボ４': 'Sub Combo 4',
 'サブコンボ５': 'Sub Combo 5', 'パージ': 'Purge', '追い討ちコンボ': 'Pursuit Combo',
 '①押しながら□': 'Hold ① + □', '①押しながら○': 'Hold ① + ○', '①押しながら△': 'Hold ① + △', '①押しながら×': 'Hold ① + ×',
 '①押しながら⑤': 'Hold ① + ⑤', '①押しながら⑦': 'Hold ① + ⑦', '①押しながら□□': 'Hold ① + □□',
 '①押しながら○○': 'Hold ① + ○○', '①押しながら○○○': 'Hold ① + ○○○', '①押しながら□□□□□': 'Hold ① + □□□□□',
}
MENU3010 = {
 '終了：⑪\u3000スキップ：○': 'Exit: ⑪  Skip: ○', 'オペレーションボーナス': 'Operation Bonus',
 'Ｏｐｅｒａｔｉｏｎ\u3000Ｐｌａｎ': 'Operation Plan', 'Ｏｐｅｒａｔｉｏｎ\u3000Ｓｔａｔｅ': 'Operation State',
 'オペレーション': 'Operation', 'ブリーフィング': 'Briefing', 'デブリーフィング': 'Debriefing', '世界情勢': 'World Situation',
 'オセアニア': 'Oceania', '日本': 'Japan', 'アラスカ列島': 'Alaskan Islands', 'アフリカ': 'Africa',
 '地球上空宙域': 'Earth Orbit', 'Ｌ２周辺宙域': 'L2 Space', '南アメリカ': 'South America', '月宙域': 'Lunar Space',
 '中国': 'China', '地球圏宙域': 'Earth Sphere', '北アメリカ': 'North America', 'ヨーロッパ': 'Europe', '火星': 'Mars',
 '土星': 'Saturn', '太平洋': 'Pacific Ocean', '地球宙域': 'Earth Space', '模擬戦域': 'Mock Battlefield',
 'トリントン基地': 'Torrington Base', 'オーストラリア北部': 'Northern Australia', '東京湾': 'Tokyo Bay',
 'アフリカ東部': 'East Africa',
 'キンバライド基地': 'Kimberide Base',            # TENTATIVE (Dragonar)
 'コンペイトウ宙域': 'Konpei Island Area',        # TENTATIVE (Gundam 0083)
 'ラビアンローズ宙域': 'La Vie en Rose Area',      # TENTATIVE (Gundam 0083)
 'ソーラ・システム周辺': 'Near the Solar System',  # TENTATIVE (Gundam 0083 weapon)
 '月面': 'Lunar Surface', '日本近海': 'Japanese Waters', '中国\u3000内陸部': 'Inland China', '暗礁宙域': 'Shoal Zone',
 '月周辺宙域': 'Lunar Vicinity',
 'ギガノス要塞\u3000内部': 'Inside Gigano Fortress',  # TENTATIVE (Dragonar: Gigano/Giganos)
 '南大西洋': 'South Atlantic', '北アメリカ\u3000内陸部': 'Inland North America', 'ロシア西部': 'Western Russia',
 'クルスク工業地帯': 'Kursk Industrial Zone', 'サセボ近海': 'Sasebo Waters', 'サセボ沿岸': 'Sasebo Coast',
 '月上空宙域': 'Lunar Orbit', '太平洋\u3000海上': 'Pacific Ocean, at Sea', 'マクロス\u3000内部': 'Inside the Macross',
 '土星宙域': 'Saturn Space', '北アメリカ\u3000東部': 'Eastern North America', 'ランタオ島近海': 'Lantau Island Waters',
 '防空衛星\u3000内部': 'Inside the Air Defense Satellite', '地球上空': 'Above Earth',
 'ボドル旗艦': 'Boddole Flagship',                # TENTATIVE (Macross)
}


def write(table, mapping):
    rows = json.load(open(EN % table, encoding='utf-8'))['rows']
    fill, missing = {}, []
    for i, r in enumerate(rows):
        key = r['jp'] if r['jp'] in mapping else r['jp'].replace(' ', '　')
        if key in mapping:
            fill[str(i)] = mapping[key]
        else:
            missing.append(r['jp'])
    unused = set(mapping) - {r['jp'] for r in rows} - {r['jp'].replace(' ', '　') for r in rows}
    json.dump(fill, open(FILL % table, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%s: %d/%d rows filled; untranslated %r; keys not in table %r' % (table, len(fill), len(rows), missing, sorted(unused)))


if __name__ == '__main__':
    write('hud3020', HUD3020)
    write('menu3010', MENU3010)
