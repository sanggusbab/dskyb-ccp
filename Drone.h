// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Drone.generated.h"

UCLASS()
class MY2_API ADrone : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ADrone();

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Mesh")
		UStaticMeshComponent* DroneMesh;

	// EditAnywhere 속성을 사용하여 에디터에서 수정 가능하도록 설정
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Drone Settings")
		FVector DroneLocation;

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
