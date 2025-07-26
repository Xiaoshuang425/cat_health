import uuid
import base64
from fastapi import APIRouter, HTTPException
from models.schemas import FecesAnalysisRequest, AnalysisResponse
from core.ai_service import analyze_feces_image
from services.notification import send_health_alert

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def create_analysis(request: FecesAnalysisRequest):
    """
    接收糞便圖像進行分析，並返回結構化結果。
    - **cat_id**: 貓咪的唯一標識符。
    - **image_base64**: 糞便圖像的Base64編碼字符串。
    """
    try:
        # 解碼Base64圖像數據
        image_data = base64.b64decode(request.image_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="無效的Base64圖像數據")

    # 調用AI服務進行分析 (目前為模擬)
    analysis_result = analyze_feces_image(image_data)

    # 檢查是否需要發送健康警報
    send_health_alert(request.cat_id, analysis_result)

    response = AnalysisResponse(
        request_id=str(uuid.uuid4()),
        cat_id=request.cat_id,
        result=analysis_result
    )

    return response