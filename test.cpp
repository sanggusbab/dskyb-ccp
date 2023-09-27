// Fill out your copyright notice in the Description page of Project Settings.


#include "test.h"
#include "Drone.h"



// Sets default values
Atest::Atest()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	UE_LOG(LogTemp, Log, TEXT("Constructor"));
	DroneClass = ADrone::StaticClass(); //추가한 코드
}

// Called when the game starts or when spawned
void Atest::BeginPlay()
{
	Super::BeginPlay();

	FString path;
	path = FPaths::ProjectContentDir() + "test/test1.txt";
	if (FPaths::FileExists(path))
	{
		FString fileContents;
		if (FFileHelper::LoadFileToString(fileContents, *path))
		{
			TArray<FString> Lines;
			fileContents.ParseIntoArrayLines(Lines);
			// 각 줄을 파싱하여 드론 오브젝트 생성
			for (const FString& Line : Lines)
			{
				TArray<FString> Tokens;
				Line.ParseIntoArray(Tokens, TEXT(","), true);
				if (Tokens.Num() == 4)
				{
					int32 DroneID = FCString::Atoi(*Tokens[0]);
					float LocX = FCString::Atof(*Tokens[1]);
					float LocY = FCString::Atof(*Tokens[2]);
					float LocZ = FCString::Atof(*Tokens[3]);
					UE_LOG(LogTemp, Log, TEXT("%d %f %f %f"), DroneID, LocX, LocY, LocZ);

					// 드론 오브젝트 생성 및 위치 설정
					FVector SpawnLocation(LocX, LocY, LocZ);
					// 드론 오브젝트 생성
					AActor* NewDrone = GetWorld()->SpawnActor<AActor>(DroneClass, SpawnLocation, FRotator::ZeroRotator);


					if (NewDrone)
					{
						UE_LOG(LogTemp, Log, TEXT("Oh my god!"));

						/*
						// 스피어 액터에 구체 메시 컴포넌트를 추가
						UStaticMeshComponent* SphereMeshComponent = NewDrone->CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Mesh"));

						// 구체 메시를 설정 (프로젝트에 포함된 구체 메시 또는 엔진에서 제공하는 기본 구체 메시를 사용할 수 있음)
						static ConstructorHelpers::FObjectFinder<UStaticMesh> SphereMeshAsset(TEXT("StaticMesh'/Game/StarterContent/Shapes/Shape_Sphere.Shape_Sphere'"));

						if (SphereMeshAsset.Succeeded())
						{
							SphereMeshComponent->SetStaticMesh(SphereMeshAsset.Object);
						}

						// 구체 액터의 렌더링 설정 또는 다른 원하는 설정을 추가할 수 있습니다.
						// 이 부분에서 새로 생성한 드론 오브젝트를 원하는 방식으로 설정할 수 있습니다.
						// 예를 들어, 드론 모델, 텍스처, 물리 설정 등을 지정할 수 있습니다.
						 // 드론 액터의 현재 위치 얻기
						FVector DroneLocation = NewDrone->GetActorLocation();
						// 드론 액터의 위치를 로그에 출력
						UE_LOG(LogTemp, Log, TEXT("Drone Location: %s"), *DroneLocation.ToString());
						
						*/
						
					}
				}
			}
		}
	}

		

	UE_LOG(LogTemp, Log, TEXT("!!!!!path : %s"), *path);


}

// Called every frame
void Atest::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

