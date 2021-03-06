﻿#!/usr/bin/env python

import base64
import csv
import requests
import urllib

api = 'http://localhost:18469/api/v1'
OB_USERNAME = "username"
OB_PASSWORD = "password"
imagehost = "http://imagehost.url.com/notrailingslash"


currency_codes = ("AED", "ARS", "AUD", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "ILS",
                  "INR", "JPY", "KRW", "MAD", "MXN", "NOK", "NZD", "PHP", "PLN", "RUB", "SEK", "SGD", "THB", "TRY",
                  "USD", "ZAR")

SHIPPING_ORIGIN = "UNITED_STATES"
# For shipping origin please choose a country code string for where you want listings to
# come from.
#
# enum CountryCode {
#     NA                             = 0; // Use this for digital goods or services
#     ALL                            = 1;
#     NORTH_AMERICA                  = 2;
#     SOUTH_AMERICA                  = 3;
#     EUROPE                         = 4;
#     AFRICA                         = 5;
#     ASIA                           = 6;
#     ALBANIA                        = 7;
#     ALGERIA                        = 8;
#     AMERICAN_SAMOA                 = 9;
#     ANDORRA                        = 10;
#     ANGOLA                         = 11;
#     ANGUILLA                       = 12;
#     ANTIGUA                        = 13;
#     ARGENTINA                      = 14;
#     ARMENIA                        = 15;
#     ARUBA                          = 16;
#     AUSTRALIA                      = 17;
#     AUSTRIA                        = 18;
#     AZERBAIJAN                     = 19;
#     BAHAMAS                        = 20;
#     BAHRAIN                        = 21;
#     BANGLADESH                     = 22;
#     BARBADOS                       = 23;
#     BELARUS                        = 24;
#     BELGIUM                        = 25;
#     BELIZE                         = 26;
#     BENIN                          = 27;
#     BERMUDA                        = 28;
#     BHUTAN                         = 29;
#     BOLIVIA                        = 30;
#     BONAIRE_SINT_EUSTATIUS_SABA    = 31;
#     BOSNIA                         = 32;
#     BOTSWANA                       = 33;
#     BOUVET_ISLAND                  = 34;
#     BRAZIL                         = 35;
#     BRITISH_INDIAN_OCEAN_TERRITORY = 36;
#     BRUNEI_DARUSSALAM              = 37;
#     BULGARIA                       = 38;
#     BURKINA_FASO                   = 39;
#     BURUNDI                        = 40;
#     CABO_VERDE                     = 41;
#     CAMBODIA                       = 42;
#     CAMEROON                       = 43;
#     CANADA                         = 44;
#     CAYMAN_ISLANDS                 = 45;
#     CENTRAL_AFRICAN_REPUBLIC       = 46;
#     CHAD                           = 47;
#     CHILE                          = 48;
#     CHINA                          = 49;
#     CHRISTMAS_ISLAND               = 50;
#     COCOS_ISLANDS                  = 51;
#     COLOMBIA                       = 52;
#     COMOROS                        = 53;
#     CONGO_REPUBLIC                 = 54;
#     CONGO                          = 55;
#     COOK_ISLANDS                   = 56;
#     COSTA_RICA                     = 57;
#     COTE_DIVOIRE                   = 58;
#     CROATIA                        = 59;
#     CUBA                           = 60;
#     CURACAO                        = 61;
#     CYPRUS                         = 62;
#     CZECH_REPUBLIC                 = 63;
#     DENMARK                        = 64;
#     DJIBOUTI                       = 65;
#     DOMINICA                       = 66;
#     DOMINICAN_REPUBLIC             = 67;
#     ECUADOR                        = 68;
#     EGYPT                          = 69;
#     EL_SALVADOR                    = 70;
#     EQUATORIAL_GUINEA              = 71;
#     ERITREA                        = 72;
#     ESTONIA                        = 73;
#     ETHIOPIA                       = 74;
#     FALKLAND_ISLANDS               = 75;
#     FAROE_ISLANDS                  = 76;
#     FIJI                           = 77;
#     FINLAND                        = 78;
#     FRANCE                         = 79;
#     FRENCH_GUIANA                  = 80;
#     FRENCH_POLYNESIA               = 81;
#     FRENCH_SOUTHERN_TERRITORIES    = 82;
#     GABON                          = 83;
#     GAMBIA                         = 84;
#     GEORGIA                        = 85;
#     GERMANY                        = 86;
#     GHANA                          = 87;
#     GIBRALTAR                      = 88;
#     GREECE                         = 89;
#     GREENLAND                      = 90;
#     GRENADA                        = 91;
#     GUADELOUPE                     = 92;
#     GUAM                           = 93;
#     GUATEMALA                      = 94;
#     GUERNSEY                       = 95;
#     GUINEA                         = 96;
#     GUINEA_BISSAU                  = 97;
#     GUYANA                         = 98;
#     HAITI                          = 99;
#     HEARD_ISLAND                   = 100;
#     HOLY_SEE                       = 101;
#     HONDURAS                       = 102;
#     HONG_KONG                      = 103;
#     HUNGARY                        = 104;
#     ICELAND                        = 105;
#     INDIA                          = 106;
#     INDONESIA                      = 107;
#     IRAN                           = 108;
#     IRAQ                           = 109;
#     IRELAND                        = 110;
#     ISLE_OF_MAN                    = 111;
#     ISRAEL                         = 112;
#     ITALY                          = 113;
#     JAMAICA                        = 114;
#     JAPAN                          = 115;
#     JERSEY                         = 116;
#     JORDAN                         = 117;
#     KAZAKHSTAN                     = 118;
#     KENYA                          = 119;
#     KIRIBATI                       = 120;
#     NORTH_KOREA                    = 121;
#     SOUTH_KOREA                    = 122;
#     KUWAIT                         = 123;
#     KYRGYZSTAN                     = 124;
#     LAO                            = 125;
#     LATVIA                         = 126;
#     LEBANON                        = 127;
#     LESOTHO                        = 128;
#     LIBERIA                        = 129;
#     LIBYA                          = 130;
#     LIECHTENSTEIN                  = 131;
#     LITHUANIA                      = 132;
#     LUXEMBOURG                     = 133;
#     MACAO                          = 134;
#     MACEDONIA                      = 135;
#     MADAGASCAR                     = 136;
#     MALAWI                         = 137;
#     MALAYSIA                       = 138;
#     MALDIVES                       = 139;
#     MALI                           = 140;
#     MALTA                          = 141;
#     MARSHALL_ISLANDS               = 142;
#     MARTINIQUE                     = 143;
#     MAURITANIA                     = 144;
#     MAURITIUS                      = 145;
#     MAYOTTE                        = 146;
#     MEXICO                         = 147;
#     MICRONESIA                     = 148;
#     MOLDOVA                        = 149;
#     MONACO                         = 150;
#     MONGOLIA                       = 151;
#     MONTENEGRO                     = 152;
#     MONTSERRAT                     = 153;
#     MOROCCO                        = 154;
#     MOZAMBIQUE                     = 155;
#     MYANMAR                        = 156;
#     NAMIBIA                        = 157;
#     NAURU                          = 158;
#     NEPAL                          = 159;
#     NETHERLANDS                    = 160;
#     NEW_CALEDONIA                  = 161;
#     NEW_ZEALAND                    = 162;
#     NICARAGUA                      = 163;
#     NIGER                          = 164;
#     NIGERIA                        = 165;
#     NIUE                           = 166;
#     NORFOLK_ISLAND                 = 167;
#     NORTHERN_MARIANA_ISLANDS       = 168;
#     NORWAY                         = 169;
#     OMAN                           = 170;
#     PAKISTAN                       = 171;
#     PALAU                          = 172;
#     PANAMA                         = 173;
#     PAPUA_NEW_GUINEA               = 174;
#     PARAGUAY                       = 175;
#     PERU                           = 176;
#     PHILIPPINES                    = 177;
#     PITCAIRN                       = 178;
#     POLAND                         = 179;
#     PORTUGAL                       = 180;
#     PUERTO_RICO                    = 181;
#     QATAR                          = 182;
#     REUNION                        = 183;
#     ROMANIA                        = 184;
#     RUSSIA                         = 185;
#     RWANDA                         = 186;
#     SAINT_BARTHELEMY               = 187;
#     SAINT_HELENA                   = 188;
#     SAINT_KITTS                    = 189;
#     SAINT_LUCIA                    = 190;
#     SAINT_MARTIN                   = 191;
#     SAINT_PIERRE                   = 192;
#     SAINT_VINCENT                  = 193;
#     SAMOA                          = 194;
#     SAN_MARINO                     = 195;
#     SAO_TOME                       = 196;
#     SAUDI_ARABIA                   = 197;
#     SENEGAL                        = 198;
#     SERBIA                         = 199;
#     SEYCHELLES                     = 200;
#     SIERRA_LEONE                   = 201;
#     SINGAPORE                      = 202;
#     SINT_MAARTEN                   = 203;
#     SUCRE                          = 204;
#     SLOVAKIA                       = 205;
#     SLOVENIA                       = 206;
#     SOLOMON_ISLANDS                = 207;
#     SOMALIA                        = 208;
#     SOUTH_AFRICA                   = 209;
#     SOUTH_SUDAN                    = 210;
#     SPAIN                          = 211;
#     SRI_LANKA                      = 212;
#     SUDAN                          = 213;
#     SURINAME                       = 214;
#     SVALBARD                       = 215;
#     SWAZILAND                      = 216;
#     SWEDEN                         = 217;
#     SWITZERLAND                    = 218;
#     SYRIAN_ARAB_REPUBLIC           = 219;
#     TAIWAN                         = 220;
#     TAJIKISTAN                     = 221;
#     TANZANIA                       = 222;
#     THAILAND                       = 223;
#     TIMOR_LESTE                    = 224;
#     TOGO                           = 225;
#     TOKELAU                        = 226;
#     TONGA                          = 227;
#     TRINIDAD                       = 228;
#     TUNISIA                        = 229;
#     TURKEY                         = 230;
#     TURKMENISTAN                   = 231;
#     TURKS_AND_CAICOS_ISLANDS       = 232;
#     TUVALU                         = 233;
#     UGANDA                         = 234;
#     UKRAINE                        = 235;
#     UNITED_ARAB_EMIRATES           = 236;
#     UNITED_KINGDOM                 = 237;
#     UNITED_STATES                  = 238;
#     URUGUAY                        = 239;
#     UZBEKISTAN                     = 240;
#     VANUATU                        = 241;
#     VENEZUELA                      = 242;
#     VIETNAM                        = 243;
#     VIRGIN_ISLANDS_BRITISH         = 244;
#     VIRGIN_ISLANDS_US              = 245;
#     WALLIS_AND_FUTUNA              = 246;
#     WESTERN_SAHARA                 = 247;
#     YEMEN                          = 248;
#     ZAMBIA                         = 249;
#     ZIMBABWE                       = 250;
#     AFGHANISTAN                    = 251;
#     ALAND_ISLANDS                  = 252;
# }

with open('listings.csv', 'rU') as f:
    reader = csv.DictReader(f, delimiter=',')

    s = requests.Session()
    payload = {'username': OB_USERNAME, 'password': OB_PASSWORD}
    login = s.post('%s/login' % api, data=payload)
    print login.json()

    for listing in reader:
        #print listing

	# Set URL of image based on SKU and imagehost url
	imageurl = imagehost + '/' + listing['SKU'] + '.jpg'
	shadeimageurl = imagehost + '/' + listing['SKU'] + '-shade.jpg'
	#print imageurl

        # Download images from listing
        ## Will need to split 'Pictures' field as it may contain multiples separated by a comma, I believe
        ## Those who have local paths to the images in their SixBit install will not be able to include images
	image = urllib.urlopen(imageurl)
        image_64 = base64.encodestring(image.read())

        # Upload to server and get hash
        payload = {
            'image': image_64
        }
        image_hashes = s.post('%s/upload_image' % api, data=payload)
	image_hashes = image_hashes.json()

        # Using tags from "eBay Title" heading which had keywords that were appended to sellers ebay listing title
	tags = listing['eBay Title']
	tags = tags.replace('[[Shade]] ', '')
	tags = tags.replace('[[MyShade]] ', '')
	tags = tags.replace('[[My Shade]] ', '')
	tags = tags.replace('[[MyProductLine]] ', '')
	tags = tags.replace(' ', ', ')

        # Separate comma-separated tags
	tags = [x.strip() for x in tags.split(',')]


	# Strip some common unnecessary eBay Title keywords
	title = listing['Title']
	title = title.replace('U Pick Choice', '')	
	title = title.replace('U Pick', '')

	# Strip some eBay html formatting from description html code
	description = listing['eBay Description']
	description = description.replace('[/n]', '')
	# Replace Sellers's eBay variables with live data
	description = description.replace('[[MyProductLine]]', title)

	# Add the *-shade.jpg to the description
	#print shadeimageurl
	description = description.replace('[[Shade]]', listing['Variation1'] + "<p><IMG SRC=\"" + shadeimageurl + "\">")
	description = description.replace('Your Choice', listing['Variation1'] + "<p><IMG SRC=\"" + shadeimageurl + "\">")
	description = description.replace('[[My Shade]]', listing['Variation1'] + "<p><IMG SRC=\"" + shadeimageurl + "\">")
	

        # Insert listing into OB
        payload = {
            'keywords': tags,
            'title': title + ' ' + listing['Variation1'], #I added Variation1 to the title because my listings are variation listings
            'description': description,
            'currency_code': 'USD',
            'price': listing['Fixed Price'],
            'process_time': '24 hours',
            'images': image_hashes['image_hashes'],
            'expiration_date': '',
            'metadata_category': 'physical good',
            'nsfw': 'false',
            'terms_conditions': '',
            'returns': 'none',
            'shipping_currency_code': 'USD',
            'shipping_domestic': 'true',
            'shipping_international': 'false',
            'category': listing['eBay Store Category2Name'],
            'condition': 'New',
            'sku': listing['SKU'],
            'free_shipping': 'true',
            'ships_to': 'UNITED_STATES',
            'shipping_origin': SHIPPING_ORIGIN
        }
        posted = s.post('%s/contracts' % api, data=payload)
        print posted.json()
