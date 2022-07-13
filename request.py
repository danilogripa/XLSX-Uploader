import requests

url = 'http://192.168.1.66:5000/convert'
myobj = {
    "os": "ios",
    "ag": "yes",
    "type": "imp",

    "key": "https://app.appsflyer.com/{app_id}?pid={appsflyer_pid}&af_prt={appsflyer_prt}&c={campaign_id}&clickid={partner_click_id}&af_channel={sub_partner_id}&af_siteid={site_id}&af_adset={creative_set_id}&af_ad_id={creative_id}&af_ad_type={creative_type}&af_adsize={creative_size}&advertising_id={aaid}&idfa={idfa}&af_cost_model={cost_model}&af_cost_currency=USD&af_cost_value={cost_value_usd}&is_retargeting={is_retargeting}&af_sub1={sub_param_1}&af_sub2={sub_param_2}&af_sub3={sub_param_3}&af_sub4={sub_param_4}&af_sub5={sub_param_5}&af_click_lookback={click_lookback}&sha1_advertising_id={aaid_sha1}&tg_click_id={click_id}",

    "tg": "https://click.trafficguard.ai?app_id=id1371054563&idfa={sub3}&partner_id=ai_markit&partner_click_id={clickid}&sub_partner_id={sub2}&site_id={pid}&tg_ver=2",

    "af": "https://app.appsflyer.com/id1371054563?pid=gogamebridge_int&af_siteid={aff}&af_ad_id={offer_id}&af_adset=%7Boffer_name%7D&af_adset_id=%7Boffer_id%7D&af_click_lookback=7d&clickid={transaction_id}&advertising_id={gaid}&idfa={idfa}&android_id={android_id}&packagename={pkg}&af_lang={lang}&af_ua={ua}&af_ip={ip}&af_prt=aimarkit&c=UK_CPA&af_adset=Football_30&af_ad=300*250&af_ios_store_cpp=f4e976ec-bb93-4d4a-8db4-078e50f1e3b7",

    "result": "https://click.trafficguard.ai/?app_id=id1371054563&source_id=gogamebridge_int&appsflyer_pid=gogamebridge_int&agency_id=ai_markit&appsflyer_prt=aimarkit&partner_click_id={transaction_id}&site_id={aff}&creative_id={offer_id}&creative_set_id=Football_30&click_lookback=7d&idfa={idfa}&campaign_id=UK_CPA&x_af_adset_id={offer_id}&x_android_id={android_id}&x_packagename={pkg}&x_af_ad=300*250&x_af_ios_store_cpp=f4e976ec-bb93-4d4a-8db4-078e50f1e3b7&x_af_lang={lang}&x_af_ua={ua}&x_af_ip={ip}&tg_ver=2"

}


x = requests.post(url, json = myobj)

print(x.text)
