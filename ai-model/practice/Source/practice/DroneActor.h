// DroneActor.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Pawn.h"
#include "Components/StaticMeshComponent.h" 
#include "DroneActor.generated.h"

UCLASS()
class PRACTICE_API ADroneActor : public APawn
{
	GENERATED_BODY()

public:
	// Sets default values for this actor's properties
	ADroneActor();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Moved to public section
	virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;

private:
	FVector TargetPosition;
	bool bIsMoving = false;

	UPROPERTY(VisibleAnywhere)
		UStaticMeshComponent* Mesh;

private:
	UFUNCTION()
		void OnMoveDrone();
};
