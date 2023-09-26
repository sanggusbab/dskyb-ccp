// DroneActor.cpp

#include "DroneActor.h"
#include "Misc/FileHelper.h"
#include "Misc/Paths.h"

// Sets default values
ADroneActor::ADroneActor()
{
	PrimaryActorTick.bCanEverTick = false;

	Mesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Mesh"));
	static ConstructorHelpers::FObjectFinder<UStaticMesh> MeshAsset(TEXT("StaticMesh'/Game/StarterContent/Shapes/Shape_Cube.Shape_Cube'"));
	if (MeshAsset.Succeeded())
	{
		Mesh->SetStaticMesh(MeshAsset.Object);
		static ConstructorHelpers::FObjectFinder<UMaterial> MaterialAsset(TEXT("Material'/Game/StarterContent/Materials/M_Brick_Clay_New.M_Brick_Clay_New'"));
		if (MaterialAsset.Succeeded())
		{
			Mesh->SetMaterial(0, MaterialAsset.Object);
		}
	}

	RootComponent = Mesh;

	AutoPossessPlayer = EAutoReceiveInput::Player0;
}

void ADroneActor::BeginPlay()
{
	Super::BeginPlay();
}

void ADroneActor::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	if (bIsMoving)
	{
		FVector NewPosition = FMath::VInterpTo(GetTransform().GetLocation(), TargetPosition, DeltaTime, 1.f);
		SetActorLocation(NewPosition);

		if (NewPosition.Equals(TargetPosition, 1.f))
		{
			bIsMoving = false;
		}
	}

	// Get the actor's location.
	FVector Location = GetActorLocation();

	// Convert the location to a string.
	FString LocationString = FString::Printf(TEXT("X: %.2f, Y: %.2f, Z: %.2f"), Location.X, Location.Y, Location.Z);

	// Display the location on screen.
	if (GEngine)
	{
		GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, LocationString);
	}
}


void ADroneActor::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
	Super::SetupPlayerInputComponent(PlayerInputComponent);

	PlayerInputComponent->BindAction("MoveDrone", IE_Pressed, this, &ADroneActor::OnMoveDrone);
}

void ADroneActor::OnMoveDrone()
{
	FString fileContents;
	FFileHelper::LoadFileToString(fileContents, *(FPaths::ProjectDir() + TEXT("coordinate.txt")));

	TArray<FString> coordinates;
	fileContents.ParseIntoArray(coordinates, TEXT(","), true);

	if (coordinates.Num() == 3)
	{
		float X = FCString::Atof(*coordinates[0]);
		float Y = FCString::Atof(*coordinates[1]);
		float Z = FCString::Atof(*coordinates[2]);

		TargetPosition = FVector(X, Y, Z);
		bIsMoving = true;
	}
}
