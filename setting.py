RANDOM_DELAY_ACCOUNT = (0, 0)
RANDOM_ACCOUNT = "ĐANG UPDATE"
RANDOM_DELAY_REQUEST = (0, 0)
MAX_THREADS_TOOL = 20
MAX_THREADS_ACCOUNT = 20
RUN_ALL_TOOL = "ON"
SLEEP_TOOL = ()
#Tùy chỉnh cấu hình từng tool
SETTING = {}
SETTING['bunny'] = {
  "DELAY": 600,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_CLICK": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_CHƠI_GAME_PUZZLE": "ON",
  "AUTO_NÂNG_CẤP_THẺ": "ON",
  "AUTO_SỬ_DỤNG_BOOSTER": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_BOOSTER": {
    "MAX_LEVEL_TAP": 14,
    "MAX_LEVEL_ENERGY": 14,
    }
}
SETTING['cex'] = {
  "DELAY": 600,
  "AUTO_CLICK": "ON",
  "AUTO_CLAIM_CRYPTO": "ON",
  "AUTO_CLAIM_PHẦN_THƯỞNG_REF": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_NÂNG_CẤP_THẺ": "ON",
  "AUTO_ĐỔI_BTC_SANG_USD": "ON",
  "RANDOM_LƯỢT_CLICK": (300,500)
}
SETTING['dotcoin'] = {
  "DELAY": 600,
  "AUTO_CLICK": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON",
  "AUTO_NÂNG_CẤP_DTC": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_THAM_GIA_TRY_LUCKY": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_BOOSTER": {
    "MAX_LEVEL_ATTEMPTS": 11,
    "MAX_LEVEL_MULTITAP": 10,
    }
}
SETTING['timefarm'] = {
  "DELAY": 600,
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_TRẢ_LỜI_CÂU_HỎI": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_NÂNG_CẤP_ĐỒNG_HỒ": "ON",
  "AUTO_STAKING": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_ĐỒNG_HỒ": {
    "MAX_LEVEL": 8,
    }
}
SETTING['wormfare'] = {
  "DELAY": 600,
  "RANDOM_LƯỢT_CLICK": (50, 100),
  "AUTO_CLICK": "ON",
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_SỬ_DỤNG_BOOSTER": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_BOOSTER": {
    "MAX_LEVEL_TAP": 11,
    "MAX_LEVEL_ENERGY": 11,
    "MAX_LEVEL_RECOVERY": 21,
    }
}
SETTING['yescoin'] = {
  "DELAY": 900,
  "RANDOM_LƯỢT_CLICK": (100, 500),
  "AUTO_CLICK": "ON",
  "AUTO_CLAIM_OFFLINE": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_SỬ_DỤNG_BOOSTER": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_BOOSTER": {
    "MAX_LEVEL_TAP": 6,
    "MAX_LEVEL_ENERGY": 10,
    "MAX_LEVEL_RECOVERY": 12,
    "MAX_LEVEL_BOT": 5,
    }
}
SETTING['bump'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_FAKE_LƯỢT_TAP": "ON",
  "RANDOM_FAKE_LƯỢT_TAP": (20000000, 30000000),
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON"
}
SETTING['cyber_finance'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON"
}
SETTING['djdog'] = {
  "DELAY": 900,
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_MUA_BOX": "ON",
  "AUTO_NÂNG_CẤP_LEVEL": "ON",
  "THÔNG_SỐ_NÂNG_CẤP": {
    #Nêú cái dưới 40 sẽ không thẻ mua box
    "MAX_LEVEL_BOX": 40, 
  }
}
SETTING['quackquack'] = {
  "DELAY": 900,
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_CLAIM_DUCK_GOLDEN": "ON",
  "AUTO_MUA_CFO": "ON",
  "AUTO_ACTIVE_CFO": "ON",
  "AUTO_SỬ_DỤNG_CFO": "ON"
}
SETTING['matchquest'] = {
  "DELAY": 900,
  "AUTO_LÀM_QUIZ": "ON",
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_MUA_DAILY_BOOSTER": "ON",
  "AUTO_MUA_GAME_BOOSTER": "ON",
  "AUTO_CHƠI_GAME": "ON",
  "RANDOM_ĐIỂM_CHƠI_GAME": (140,160)
}
SETTING['blum'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_CHƠI_GAME": "ON",
  "RANDOM_ĐIỂM_CHƠI_GAME": (140,160)
}
SETTING['memefi'] = {
  "DELAY": 900,
  "RANDOM_LƯỢT_CLICK": (100, 200),
  "MAX_LƯỢT_QUAY_SPIN": 1000,
  "AUTO_CLICK": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_QUAY_SPIN": "ON",
  "AUTO_KILL_BOT": "ON",
  "AUTO_SỬ_DỤNG_BOOSTER": "ON",
  "AUTO_NÂNG_CẤP_BOOSTER": "ON",
  "THÔNG_SỐ_NÂNG_CẤP_BOOSTER": {
    "MAX_LEVEL_DAMAGE": 15,
    "MAX_LEVEL_ENERGY": 8,
    #Đặt tối đa là 3 thôi nhé
    "MAX_LEVEL_RECHARGING": 3,
    }
}
SETTING['iceberg'] = {
  "DELAY": 900,
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
}
SETTING['major'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_THAM_GIA_CLAN": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_HOLD_TO_EARN": "ON",
  "AUTO_ROULETTE": "ON",
  "AUTO_SWIPE": "ON",
}
SETTING['kucoin'] = {
  "DELAY": 900,
  "AUTO_CLICK": "ON",
  #Tối đa 60 lượt click
  "RANDOM_LƯỢT_CLICK": (30, 60),
  "ENERGY_VÔ_HẠN": "ON",
}
SETTING['midas'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_TAPING": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
}
SETTING['atx'] = {
  "DELAY": 900,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
}
SETTING['fastmint'] = {
  "DELAY": 600,
  "AUTO_START_FARM": "ON",
  "AUTO_CLAIM_FARM": "ON",
  "AUTO_CLAIM_PHẦN_THƯỞNG_REF": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
  "AUTO_NÂNG_CẤP": "ON",
  "THÔNG_SỐ_NÂNG_CẤP": {
    "LEVEL_MAX": 3
  }
}
SETTING['duckcoop'] = {
  "DELAY": 600,
  "AUTO_ĐIỂM_DANH": "ON",
  "AUTO_LÀM_NHIỆM_VỤ": "ON",
}