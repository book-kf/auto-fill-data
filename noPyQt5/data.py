data ="""class Craft_Route_Items(BaseModel):
        process: str = Field(title="STPO-POSNR",min_length=1, max_length=4, description="工序")
        workCentre: str = Field(title="STPO-POSTP", min_length=1, max_length=20, description="工作中心")
        processText: str = Field(title="STPO-IDNRK", min_length=1, max_length=18, description="工序短文本")
        tableHead: Optional[str] = Field(title="STPO-MEINS", max_length=3, description="表头")
        process2: Optional[str] = Field(title="STPO-MENGE", max_length=13, description="工序")
        ctrlCode: str = Field(title="STPO-SORTF", min_length=1, max_length=10, description="控制码")
        directLabor: str = Field(title="STPO-LGORT", min_length=1, max_length=4, description="直接人工")
        time: str = Field(title="STPO-ALPGR", max_length=9, description="时间", default='')
        fuelCost: str = Field(title="STPO-ALPST", max_length=1, description="燃料费用", default='')
        time_fuel: str = Field(title="STPO-ALPRF", max_length=2, description="时间", default='')
        powerCost: str = Field(title="STPO-EWAHR", max_length=9, description="动力费用", default='')
        time_power: str = Field(title="STPO-AUSCH", max_length=10, description="时间", default='')
        DepreciationCost: str = Field(title="STPO-SCHGT", max_length=10, description="折旧费用")
        time_Depreciation: str = Field(title="TYPE", max_length=10, description="时间", default='')
        ManufactureCost: str = Field(title="STATUS", max_length=10, description="制造费用", default='')
        time_Manufacture: str = Field(title="CUKN-KNBLK", max_length=2886, description="时间", default='')
        fieldValue: Optional[str] = Field(title="STPO-ITSOB", max_length=4, description="字段键值", default='')
        seconds: Optional[str] = Field(title="STPO-POTX1", max_length=40, description="节拍（秒）", default='')
        standardNumber: Optional[str] = Field(title="CHAR", max_length=40, description="标准人数", default='')
        modePieceNumber: Optional[str] = Field(title="STPO-POTX2", max_length=40, description="一模/撬几件", default='')  # 项目文本2
        devicNumber: Optional[str] = Field(title="STPO-DUMMY", max_length=1, description="使用设备工位数", default='')  # 仅整车使用
        machineBeat: Optional[str] = Field(title="STPO-ZZHCZ", max_length=10, description="机器节拍", default='')  # 互斥组
        machineBeatUnit: Optional[str] = Field(title="STPO-ZZWLXZ", max_length=10, description="机器节拍单位",                                      default='')  # 仅精工使用，下拉选择项，代装件/载体/其他
        ratedPower: Optional[str] = Field(title="STPO-ZZRJBIM", max_length=100, description="线体额定功率",                                   default='')  # 仅整车使用如果是组件是新增，还需传输以下字段
        ratedPowerUnit: Optional[str] = Field(title="MARA-MTART", max_length=4, description="线体额定功率单位")  # 物料类型
        fuelNumber: Optional[str] = Field(title="MAKT-MAKTX", max_length=40, description="使用燃料工位数")  # 中文描述，默认语言代码CN
        isUseFuel: Optional[str] = Field(title="MAKT-SPRAS", max_length=2, description="是否用燃料", default='')  # 默认EN
        isUseMachine: Optional[str] = Field(title="MAKT-MAKTXE", max_length=40, description="是否用机械",                                            default='')  # 英文描述
        field01: Optional[str] = Field(title="字段1", description="预留字段1", default='')
        field02: Optional[str] = Field(title="字段2", description="预留字段2", default='')
        field03: Optional[str] = Field(title="字段3", description="预留字段3", default='')
        field04: Optional[str] = Field(title="字段4", description="预留字段4", default='')
        field05: Optional[str] = Field(title="字段5", description="预留字段5", default='')
        field06: Optional[str] = Field(title="字段6", description="预留字段6", default='')
        class Craft_Route_Request(BaseModel):
        materialCode: str = Field(title="物料编码", min_length=1, max_length=18, description="物料编码")
        factory: str = Field(title="工厂", min_length=1, max_length=4, description="工厂")
        processRouteGroup: str = Field(title="工艺路线组", min_length=8, max_length=8, description="工艺路线组")
        groupCounter: str = Field(title="组计数器", min_length=1, max_length=2, description="组计数器")
        processRouteGroupDesc: str = Field(title="工艺路线组描述", min_length=1, max_length=40, description="工艺路线组描述")
        effect: str = Field(title="用途",min_length=1,  max_length=3, description="用途")
        status: str = Field(title="状态",min_length=1,  max_length=3, description="状态")
        engineerNumber: Optional[str] = Field(title="工程更改号", max_length=12, description="工程更改号")
        engineerNumberDesc: Optional[str] = Field(title="工程更改号描述", max_length=40, description="工程更改号描述")
        effectiveStartDate: Optional[str] = Field(title="有效起始日期", max_length=8, description="有效起始日期")
        changeReason: Optional[str] = Field(title="更改原因", max_length=40, description="更改原因")
        field01: Optional[str] = Field(title="字段1", description="预留字段1", default='')
        field02: Optional[str] = Field(title="字段2", description="预留字段2", default='')
        field03: Optional[str] = Field(title="字段3", description="预留字段3", default='')
        field04: Optional[str] = Field(title="字段4", description="预留字段4", default='')
        field05: Optional[str] = Field(title="字段5", description="预留字段5", default='')
        items: List[Craft_Route_Items]
        class Craft_Route_RequestList(BaseModel):
        Craft_Route_List: List[Craft_Route_Request]"""