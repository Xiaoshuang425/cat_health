from fastapi import FastAPI
from api.endpoints import analysis

app = FastAPI(
    title="智能貓咪健康監測系統 API",
    description="提供貓咪糞便圖像分析和健康數據追蹤的後端服務。",
    version="1.0.0",
)

# 包含分析相關的API路由
app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "歡迎使用智能貓咪健康監測系統 API"}

# 建議在開發環境中使用以下命令啟動:
# uvicorn main:app --reload