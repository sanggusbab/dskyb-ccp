// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Misc/FileHelper.h"   // 파일 처리 관련 헤더
#include "Misc/Paths.h"       // 경로 관련 헤더
#include "Containers/Array.h" // TArray 클래스 관련 헤더
#include "UObject/ConstructorHelpers.h" // UObject 생성 관련 헤더
#include "Components/StaticMeshComponent.h" // 구체 메시를 표현하기 위한 헤더
#include "Engine/World.h"     // 월드 관련 헤더
#include "Engine/Engine.h"    // 엔진 관련 헤더
#include "test.generated.h"

UCLASS()
class MY2_API Atest : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	Atest();

protected:
	// Called when the game starts or when spawned

	UPROPERTY(EditAnywhere, Category = "Drone")
		TSubclassOf<AActor> DroneClass; // Drone 클래스를 선택하기 위한 변수
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
